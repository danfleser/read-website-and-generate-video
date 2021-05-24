import os
import subprocess

from python.common.utils import is_file_broken_size
from python.common.variables import get_videos_export_dir, get_videos_common_dir

SCREEN_RESOLUTION = {
    "WIDTH": 1920,
    "HEIGHT": 1080,
    "Y_OFFSET": 210
}


class ScreenRecord:
    def __init__(self, filename):
        self.filename = filename

        self.original_video_path = get_videos_export_dir(self.filename + '.mkv')
        self.edited_video_path = get_videos_export_dir(self.filename + 'xeditedx.mkv')

        self.subscribe_video_path = get_videos_common_dir('yt_like_sub.mov')

    def start(self):
        command = f"ffmpeg -y \
                           -f gdigrab \
                           -draw_mouse 0 \
                           -framerate 60 \
                           -offset_x 0 -offset_y {SCREEN_RESOLUTION['Y_OFFSET']} \
                           -video_size {SCREEN_RESOLUTION['WIDTH']}x{SCREEN_RESOLUTION['HEIGHT']} \
                           -i desktop \
                           -f dshow -i audio=\"CABLE Output (VB-Audio Virtual Cable)\" \
                           -c:v libx264 -qp 0 -c:a aac \
                           {self.original_video_path}"
        self.process = subprocess.Popen(command, start_new_session=True)

    def stop(self):
        self.process.terminate()

    def generate_final_video(self):
        green_color = "13FE06"

        video_cmd = f"ffmpeg \
                    -i {self.original_video_path} \
                    -i {self.subscribe_video_path} \
                    -filter_complex \"[1:v]colorkey=0x{green_color}:0.4:0.01[chkeyvid];[0:v][chkeyvid]overlay[outv];[0:a][1:a] amix [outa]\" \
                    -map \"[outv]\" -map \"[outa]\" \"{self.edited_video_path}\""
        os.system(video_cmd)

        if is_file_broken_size(self.edited_video_path):
            os.remove(self.edited_video_path)
        else:
            os.remove(self.original_video_path)

            # rename file to original name
            os.rename(self.edited_video_path, self.original_video_path)
