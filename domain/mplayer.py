"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    mplayer  
"""

from crosscutting.constants import COOKIE_FILE
from .video_player import VideoPlayer


class Mplayer(VideoPlayer):
    name = "mplayer"
    flags = "-fs -really-quiet -cookies -cookies-file {0}".format(COOKIE_FILE)

    def _get_command(self):
        return "{0} -fs -really-quiet -cookies -cookies-file".format(self.name)
