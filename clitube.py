#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    clitube  
"""

import argparse
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

        youtubedl = Youtubedl(user_url)
        video_player = get_instance_of(VIDEO_PLAYER)

        print_header()
        print_fetching(user_url)
        real_video_url = youtubedl.get_url()
        video_player.play(real_video_url)
    else:
        print_error('Requires Python {0}'.format(REQUIRED_PYTHON_VERSION))
        exit(0)
