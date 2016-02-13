"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    ioc_factory_video_player  
"""

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
