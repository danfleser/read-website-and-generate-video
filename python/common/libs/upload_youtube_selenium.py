from typing import DefaultDict, Optional
from collections import defaultdict
import json
import time
from .Constant import *
from pathlib import Path

from python.common.libs.Firefox import Firefox, By


def load_metadata(metadata_json_path: Optional[str] = None) -> DefaultDict[str, str]:
    if metadata_json_path is None:
        return defaultdict(str)
    with open(metadata_json_path, encoding="utf-8") as metadata_json_file:
        return defaultdict(str, json.load(metadata_json_file))


class YouTubeUploader:
    def __init__(self, headless, cookie_working_dir: Optional[str] = None) -> None:
        if cookie_working_dir:
            self.cookie_working_dir = cookie_working_dir
            self.browser = Firefox(
                cookies_folder_path=self.cookie_working_dir,
                extensions_folder_path=self.cookie_working_dir,
                headless=headless,
                full_screen=False
            )
        else:
            current_working_dir = str(Path.cwd())
            self.cookie_working_dir = current_working_dir
            self.browser = Firefox(self.cookie_working_dir, self.cookie_working_dir, headless=headless)
        self.__login()

    def __login(self):
        self.browser.get(Constant.YOUTUBE_URL)
        time.sleep(Constant.USER_WAITING_TIME)

        if self.browser.has_cookies_for_current_website():
            self.browser.load_cookies()
            time.sleep(Constant.USER_WAITING_TIME)
            self.browser.refresh()
        else:
            print('Please sign in and then press enter')
            input()
            self.browser.get(Constant.YOUTUBE_URL)
            time.sleep(Constant.USER_WAITING_TIME)
            self.browser.save_cookies()

    def upload(self, video_path: str, metadata_json_path: Optional[str] = None):
        try:
            metadata_dict = load_metadata(metadata_json_path)
            self.__validate_inputs(metadata_dict, video_path)
            return self.__upload(video_path, metadata_dict)
        except Exception as e:
            print(e)
            return False

    def __set_channel_language_english(self):
        try:
            self.browser.driver.find_element_by_id("img").click()
            time.sleep(Constant.USER_WAITING_TIME)
            self.browser.driver.find_element_by_xpath("(//yt-icon[@id='right-icon'])[6]").click()
            time.sleep(Constant.USER_WAITING_TIME)
            self.browser.driver.find_element_by_xpath("(//yt-formatted-string[@id='label'])[26]").click()
            time.sleep(Constant.USER_WAITING_TIME)
        except:
            pass

    def __upload(self, video_path: str, metadata_dict: DefaultDict[str, str] = None) -> (bool, Optional[str]):
        self.browser.get(Constant.YOUTUBE_URL)
        time.sleep(Constant.USER_WAITING_TIME)

        # set english as language
        self.__set_channel_language_english()

        self.browser.get(Constant.YOUTUBE_UPLOAD_URL)
        time.sleep(5)

        # attach video
        absolute_video_path = str(Path.cwd() / video_path)
        self.browser.find(By.XPATH, Constant.INPUT_FILE_VIDEO).send_keys(absolute_video_path)
        time.sleep(5)

        # Catch max uploads/day limit errors
        next_button = self.browser.find(By.ID, Constant.NEXT_BUTTON)
        if next_button.get_attribute('hidden') == 'true':
            error_short_by_xpath = self.browser.find(By.XPATH, Constant.ERROR_SHORT_XPATH)
            print(f"ERROR: {error_short_by_xpath.text} {self.cookie_working_dir}")
            return False

        # set title & description
        title_and_description = self.browser.driver.find_elements_by_css_selector(Constant.title_description_containers)

        # set title
        title_field = title_and_description[0]
        title_field.click()
        time.sleep(Constant.USER_WAITING_TIME)
        title_field.clear()
        time.sleep(Constant.USER_WAITING_TIME)
        title_field.send_keys(metadata_dict[Constant.VIDEO_TITLE])

        # set description
        description_field = title_and_description[1]
        description_field.click()
        time.sleep(Constant.USER_WAITING_TIME)
        description_field.clear()
        time.sleep(Constant.USER_WAITING_TIME)
        description_field.send_keys(metadata_dict[Constant.VIDEO_DESCRIPTION])
        time.sleep(Constant.USER_WAITING_TIME)

        # set thumbnail
        thumbnail = metadata_dict[Constant.VIDEO_THUMBNAIL]
        if thumbnail != '':
            absolute_thumbnail_path = str(Path.cwd() / thumbnail)
            self.browser.find(By.XPATH, Constant.INPUT_FILE_THUMBNAIL).send_keys(
                absolute_thumbnail_path)
            change_display = "document.getElementById('file-loader').style = 'display: block! important'"
            self.browser.driver.execute_script(change_display)
            time.sleep(5)

        # go to VISIBILITY tab by the section badges 2021 feature
        self.browser.driver.find_element_by_id("step-badge-3").click()

        # set VISIBILITY public
        visibility_main_button = self.browser.find(By.NAME, Constant.PUBLIC_BUTTON)
        self.browser.find(By.ID, Constant.RADIO_LABEL, visibility_main_button).click()

        # wait until video uploads
        uploading_progress_container = self.browser.find(By.CSS_SELECTOR, Constant.UPLOADING_PROGRESS_SELECTOR)
        while True:
            in_process = uploading_progress_container.text.find(Constant.UPLOADED) == -1
            if in_process:
                time.sleep(5)
            else:
                break

        try:
            done_button = self.browser.find(By.ID, Constant.DONE_BUTTON)
            # Catch such error as
            # "File is a duplicate of a video you have already uploaded"
            if done_button.get_attribute('aria-disabled') == 'true':
                error_message = self.browser.find(By.XPATH, Constant.ERROR_CONTAINER).text
                print(error_message)

            done_button.click()
            print("Published the video with video_id = {}".format(self.__get_video_id()))
            time.sleep(Constant.USER_WAITING_TIME)
        except Exception as e:
            print(e)
            pass

        return True

    def __is_videos_available(self):
        # if there are no videos to be deleted, this element should be visible
        # if not visible throw error, and proceed to delete more videos
        try:
            self.browser.driver.find_element_by_xpath("//ytcp-video-section-content[@id='video-list']/div/div[2]/div")
            # return True, there are no more video to be deleted
            return True
        except:
            return False

    def close_youtube_annoying_popup(self):
        self.browser.execute_script(
            "document.querySelectorAll('ytcp-feature-discovery-callout').forEach(e => e.remove())")
        time.sleep(Constant.USER_WAITING_TIME)

    def __get_video_id(self) -> Optional[str]:
        video_id = None
        try:
            video_url_container = self.browser.find(By.XPATH, Constant.VIDEO_URL_CONTAINER)
            video_url_element = self.browser.find(By.XPATH, Constant.VIDEO_URL_ELEMENT,
                                                  element=video_url_container)
            video_id = video_url_element.get_attribute(Constant.HREF).split('/')[-1]
        except:
            pass
        return video_id

    def __validate_inputs(self, metadata_dict, video_path):
        if not metadata_dict[Constant.VIDEO_TITLE]:
            print("The video title was not found in a metadata file")
            metadata_dict[Constant.VIDEO_TITLE] = Path(video_path).stem
            print("The video title was set to {}".format(Path(video_path).stem))
        if not metadata_dict[Constant.VIDEO_DESCRIPTION]:
            print("The video description was not found in a metadata file")

    def quit(self):
        self.browser.driver.quit()
