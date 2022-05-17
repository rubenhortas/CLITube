#!/usr/bin/env python
# _*_ coding:utf-8 _*
from application.handlers.exception_handler import handle_exception
from domain.mplayer import Mplayer
from domain.omxplayer import OMXplayer


def get_instance_of(video_player):
    try:
        video_player = video_player.lower()

        d = {
            "mplayer": Mplayer(),
            "omxplayer": OMXplayer()
        }

        return d.get(video_player)

    except Exception as e:
        handle_exception(e)
