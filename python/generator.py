import random

from python.screen_record import ScreenRecord
from python.setup_webdriver import ScrapeBrowser


class WebsiteToVideoGenerator:
    def __init__(self, article_url, scraper):
        filename = str(random.randint(1000000, 9000000))

        self.driver = ScrapeBrowser(article_url, scraper, filename)
        self.sr = ScreenRecord(filename)

    def generate_video(self):
        self.sr.start()
        self.driver.scrape()
        self.sr.stop()
        self.driver.quit()

        self.sr.generate_final_video()
