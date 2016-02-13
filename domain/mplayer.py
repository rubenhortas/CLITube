"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    mplayer  
"""
import os

import subprocess

from crosscutting.constants import COOKIE_FILE
from .video_player import VideoPlayer


class Mplayer(VideoPlayer):
    name = ["mplayer"]
    cookie = [COOKIE_FILE]
    flags = ["-f",
             "-really-quiet",
             "-cookies",
             "-cookies-file"
             ]

    def _get_command(self):
        return self.name + self.flags + self.cookie