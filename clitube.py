import argparse
import re
import signal

from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from config import VIDEO_PLAYER
from crosscutting.clitube_messages import print_header, print_fetching
from crosscutting.condition_messages import print_error
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from domain.video_player_factory import get_instance_of
from domain.youtubedl import Youtubedl
from presentation.utils.screen import clear_screen

YOUTUBE_VIDEO_PATTERN = re.compile("http[s]?://www.youtube.com/watch\?v=[a-zA-Z0-9]+")
# https://www.youtube.com/watch?v=iSYcAxD0VM4&list=PLC520AA0C7DF76087&index=3

if __name__ == "__main__":
    signal.signal(signal.SIGINT, exit_signal_handler)

    clear_screen()

    interpreter_version = get_interpreter_version()

    if interpreter_version == REQUIRED_PYTHON_VERSION:
        parser = argparse.ArgumentParser(prog="CLITube")
        parser = argparse.ArgumentParser(description="Script to watch youtube videos from CLI in a video player")
        parser.add_argument("youtube_url", metavar="YOUTUBE_VIDEO_URL", nargs=1, help="URL of the video on youtube.")
        args = parser.parse_args()

        user_url = args.youtube_url[0]

        match = YOUTUBE_VIDEO_PATTERN.search(user_url)

        if match:
            user_url = match.group(0)

            youtubedl = Youtubedl(user_url)
            video_player = get_instance_of(VIDEO_PLAYER)

            print_header()
            print_fetching(user_url)
            real_video_url = youtubedl.get_url()
            video_player.play(real_video_url)
        else:
            print_error('{0} is not a youtube video'.format(user_url))
            exit(0)
    else:
        print_error('Requires Python {0}'.format(REQUIRED_PYTHON_VERSION))
        exit(0)
