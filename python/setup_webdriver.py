import json
import time
import requests

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

from python.common.utils import write_json_file
from python.screen_record import SCREEN_RESOLUTION
from python.common.variables import js_init_scripts, get_scraper, get_videos_export_dir


class ScrapeBrowser:
    def __init__(self, article_url, scraper, filename):
        self.scraper = scraper
        self.article_url = article_url
        self.filename = filename

        self.__setup_options()
        self.__setup_user_agent()

        self.driver = webdriver.Chrome(options=self.options)
        self.__setup_resolution()

        self.driver.get(self.article_url)

        self.__execute_js_scraper_import_scripts()
        self.__execute_click_body_for_interaction()

    def __setup_options(self):
        self.options = Options()
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])

    def __setup_user_agent(self):
        ua = UserAgent()
        user_agent = ua.random

        self.options.add_argument(f'user-agent={user_agent}')

    def __setup_resolution(self):
        self.driver.set_window_size(SCREEN_RESOLUTION["WIDTH"] + 20,
                                    SCREEN_RESOLUTION["HEIGHT"] + SCREEN_RESOLUTION["Y_OFFSET"] + 10)
        self.driver.set_window_position(-10, 0)

    def __execute_click_body_for_interaction(self):
        self.driver.find_element_by_css_selector("header").click()
        time.sleep(1)

    def __execute_js_scraper_import_scripts(self):
        self.driver.execute_script(js_init_scripts)
        time.sleep(1)

    def scrape(self):
        time.sleep(2)
        self.driver.execute_script(get_scraper(self.scraper))
        time.sleep(1)

        self.__wait_until_page_is_read()
        self.save_metadata()

    def __wait_until_page_is_read(self):
        # wait until reading is finished
        in_progress = True
        while in_progress:
            time.sleep(5)
            in_progress = self.driver.execute_script("return window.isSpeaking()")

        time.sleep(5)

    def quit(self):
        self.driver.quit()

    def save_metadata(self):
        title = self.driver.execute_script("return window.articleTitle")
        heading_times = self.driver.execute_script("return window.headingTimes")

        thumbnail_path = self.save_image_and_get_path(
            self.filename,
            self.driver.execute_script("return window.articleThumbnailUrl")
        )

        metadata = {
            'title': title,
            'thumbnail_path': thumbnail_path,
            'description': self.get_heading_times_as_description(heading_times)
        }

        write_json_file(get_videos_export_dir(f"{self.filename}.json"), metadata)

    @staticmethod
    def get_heading_times_as_description(heading_times):
        times = json.dumps(heading_times)
        times_json = json.loads(times)

        description = "0:0:0 - Introduction\n"
        for heading in times_json:
            description += f"{heading['time']} - {heading['text']}\n"

        return description

    @staticmethod
    def save_image_and_get_path(filename, url):
        if url == '':
            return ''

        img_extension_index = url.rindex('.')
        img_extension = url[img_extension_index:]
        thumbnail_path = get_videos_export_dir(f"{filename}{img_extension}")

        # save image to local disk
        f = open(thumbnail_path, 'wb')
        f.write(requests.get(url).content)
        f.close()

        # resize image to 1280x720 resolution
        image = Image.open(thumbnail_path)
        new_image = image.resize((1280, 720))
        new_image.save(thumbnail_path)

        return thumbnail_path
