#!/usr/bin/env python
# _*_ coding:utf-8 _*
from .video_player import VideoPlayer


class OMXplayer(VideoPlayer):
    name = "omxplayer"
    flags = ""

    def __init__(self):
        self.name = "omxplayer"
        self.flags = ""

    def _get_command(self):
        return self.name + self.flags
