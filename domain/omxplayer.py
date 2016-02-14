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

    # TODO: Add flags
    flags = ""

    def _get_command(self):
        return self.name + self.flags
