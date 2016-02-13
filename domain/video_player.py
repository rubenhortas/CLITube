"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    video_player  
"""
import os
import subprocess

from application.handlers.exception_handler import handle_exception


class VideoPlayer(object):
    name = None
    flags = None

    def _get_command(self):
        raise Exception("Not implemented")

    def play(self, url):
        try:
            command = "{0} {1}".format(self._get_command(), url)
            devnull = open(os.devnull, 'w')

            p = subprocess.Popen(command, stdout=devnull, stderr=devnull, shell=True)
            p.wait()
        except Exception as e:
            handle_exception(e)
