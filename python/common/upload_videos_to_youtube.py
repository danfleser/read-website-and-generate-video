import os
import glob

from python.common.libs.upload_youtube_selenium import YouTubeUploader
from python.common.utils import load_json_file
from python.common.variables import videos_dir_path, accounts_dir


def upload_videos():
    for account_name in os.listdir(accounts_dir):
        youtube_uploader = YouTubeUploader(True, os.path.join(accounts_dir, account_name))
        list_of_video_files = glob.glob(os.path.join(videos_dir_path, 'processed', '*.mkv'))

        for _, video_path in enumerate(list_of_video_files):
            try:
                # upload to youtube
                metadata_path = video_path.replace("StackOverflow.mkv", ".json")
                uploaded = youtube_uploader.upload(video_path, metadata_path)

                if not uploaded:
                    break

                # remove file from disk
                thumbnail = load_json_file(metadata_path)['thumbnail_path']
                if thumbnail != '':
                    os.remove(thumbnail)
                os.remove(video_path)
                os.remove(metadata_path)
            except Exception as err:
                print(err)
                break

        try:
            youtube_uploader.quit()
        except:
            pass
        print(account_name)

