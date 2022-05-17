#!/usr/bin/env python
# _*_ coding:utf-8 _*
import subprocess

from application.handlers.error_handler import handle_error
from application.handlers.exception_handler import handle_exception
from crosscutting.constants import COOKIE_FILE, ENCODING


class Youtubedl:
    filesystem_options = [
        "--cookies"  # File to read cookies from and dump cookie jar in
    ]

    verbosity_options = [
        "-g",  # Simulate, quiet but print URL
    ]

    cookie = [COOKIE_FILE]
    name = ["youtube-dl"]
    youtube_url = None

    def __init__(self, youtube_url):
        self.youtube_url = [youtube_url]

    def get_url(self):
        try:
            p = subprocess.Popen(self.name + self.filesystem_options + self.cookie + self.verbosity_options +
                                 self.youtube_url, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
            p.wait()

            url, error = p.communicate()

            if error:
                handle_error(str(error, ENCODING), False)

            if url:
                return str(url.strip(), ENCODING)
            else:
                handle_error("Error fetching youtube_url", True)
        except Exception as e:
            handle_exception(e)
