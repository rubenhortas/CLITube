"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    clitube  
"""

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

YOUTUBE_PATTERN = re.compile("(http(s)?://www.youtube.com/watch\?v=(\w)*)")
URL_PATTERN = re.compile(
    "(?P<video_url>http(s)?://www.youtube.com/watch\?v=(\w)*)&list=(?P<list>(\w)*)&index=(?P<index>(\d)*)")


def __is_youtube(url):
    match = YOUTUBE_PATTERN.search(url)
    if match:
        return True
    else:
        return False


def __clean_url(url):
    match = URL_PATTERN.search(url)
    if match:
        return match.group(0)
    else:
        return url


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

        if __is_youtube(user_url):
            youtube_url = __clean_url(user_url)

            youtubedl = Youtubedl(youtube_url)
            video_player = get_instance_of(VIDEO_PLAYER)

            print_header()
            print_fetching(user_url)
            real_video_url = youtubedl.get_url()
            video_player.play(real_video_url)
        else:
            print_error('Is not a youtube video')
    else:
        print_error('Requires Python {0}'.format(REQUIRED_PYTHON_VERSION))
        exit(0)
