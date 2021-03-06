#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    omxplayer  
"""

from .video_player import VideoPlayer


class OMXplayer(VideoPlayer):
    name = "omxplayer"
    flags = ""

    def __init__(self):
        self.name = "omxplayer"
        self.flags = ""

    def _get_command(self):
        return self.name + self.flags
