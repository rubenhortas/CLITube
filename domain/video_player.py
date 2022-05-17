#!/usr/bin/env python
# _*_ coding:utf-8 _*
import subprocess

from application.handlers.error_handler import handle_error
from application.handlers.exception_handler import handle_exception
from crosscutting.condition_messages import print_info
from crosscutting.constants import ENCODING


class VideoPlayer(object):
    name = None
    flags = None

    def _get_command(self):
        raise Exception("Not implemented")

    def play(self, url):
        try:
            print_info("Using " + self.name)
            print_info("Playing {0}".format(url))

            command = "{0} \"{1}\"".format(self._get_command(), url)
            # devnull = open(os.devnull, 'w')

            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            p.wait()

            out, error = p.communicate()

            if error:
                handle_error(str(error, ENCODING), False)

            if out:
                return str(url.strip(), ENCODING)
        except Exception as e:
            handle_exception(e)
