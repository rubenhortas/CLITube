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
from domain.ioc_factory_video_player import get_instance_of
from domain.youtubedl import Youtubedl
from presentation.utils.screen import clear_screen

if __name__ == "__main__":
    signal.signal(signal.SIGINT, exit_signal_handler)

    clear_screen()

    interpreter_version = get_interpreter_version()

    if interpreter_version == REQUIRED_PYTHON_VERSION:

        parser = argparse.ArgumentParser(prog="CLITube")
        parser = argparse.ArgumentParser(description="Script to watch youtube videos from CLI in a video player")
        parser.add_argument("youtube_url", metavar="YOUTUBE VIDEO URL", nargs=1, help="URL of the video on youtube.")
        args = parser.parse_args()

        youtube_url = args.youtube_url[0]

        youtubedl = Youtubedl(youtube_url)
        video_player = get_instance_of(VIDEO_PLAYER)

        print_header()
        print_fetching(youtube_url)
        url = youtubedl.get_url()
        video_player.play(url)

    else:
        print_error('Requires Python {0}'.format(REQUIRED_PYTHON_VERSION))
        exit(0)
