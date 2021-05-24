import os
from pathlib import Path

main_dir = Path(__file__).parent.parent.parent

# js directory script names
javascript_dir_path = os.path.join(main_dir, "javascript")
javascript_website_scrapers_dir_path = os.path.join(
    javascript_dir_path, "website-scrapers")
javascript_website_scrapers_common_dir_path = os.path.join(
    javascript_website_scrapers_dir_path, "common")

# js init scripts
js_init_scripts = open(os.path.join(
    javascript_website_scrapers_common_dir_path, "1.init-scripts.js"), "r").read()
js_init_variables = open(os.path.join(
    javascript_website_scrapers_common_dir_path, "2.init-variables.js"), "r").read()
js_utils = open(os.path.join(
    javascript_website_scrapers_common_dir_path, "3.utils.js"), "r").read()
js_mapper = open(os.path.join(
    javascript_website_scrapers_common_dir_path, "4.mapper.js"), "r").read()

# js website scrapers
js_scraper_freecodecamp = open(os.path.join(
    javascript_website_scrapers_dir_path, "freecodecamp.js"), "r").read()
js_scraper_hackernoon = open(os.path.join(
    javascript_website_scrapers_dir_path, "hackernoon.js"), "r").read()
js_scraper_theverge = open(os.path.join(
    javascript_website_scrapers_dir_path, "theverge.js"), "r").read()
js_scraper_stackoverflow = open(os.path.join(
    javascript_website_scrapers_dir_path, "stackoverflow.js"), "r").read()


def get_scraper(js_scraper_code):
    return js_init_variables + "\n" + js_utils + "\n" + js_mapper + "\n" + js_scraper_code


# videos dir
videos_dir_path = os.path.join(main_dir, "videos")
videos_common_dir_path = os.path.join(videos_dir_path, "common")


def get_videos_export_dir(filename):
    return os.path.join(videos_dir_path, filename)


def get_videos_common_dir(filename):
    return os.path.join(videos_common_dir_path, filename)


# accounts
accounts_dir = os.path.join(main_dir, 'accounts')
