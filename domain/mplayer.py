from crosscutting.constants import COOKIE_FILE
from .video_player import VideoPlayer


class Mplayer(VideoPlayer):
    name = "mplayer"
    flags = "-fs -really-quiet -cookies -cookies-file {0}".format(COOKIE_FILE)

    # def __init__(self):
    #     self.name = "mplayer"
    #     self.flags = "-fs -really-quiet -cookies -cookies-file {0}".format(COOKIE_FILE)

    def _get_command(self):
        return "{0} -fs -really-quiet -cookies -cookies-file".format(self.name)
