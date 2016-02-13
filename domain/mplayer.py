"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    mplayer  
"""

from .video_player import VideoPlayer


class Mplayer(VideoPlayer):

    name = "mplayer"
    flags = "-f"
    video_file = None

    def __init__(self, video_file):
        self.video_file = video_file
