"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    youtubedl  
"""

# import re
import subprocess

from application.handlers.error_handler import handle_error
from application.handlers.exception_handler import handle_exception
# from crosscutting.condition_messages import print_info
from crosscutting.constants import COOKIE_FILE
from crosscutting.constants import ENCODING


# Network options
# --proxy URL                      Use the specified HTTP/HTTPS proxy. Pass in an empty string (--proxy "") for direct connection

# Video selection
# --yes-playlist                   Download the playlist, if the URL refers to a video and a playlist.

# Authentication options
# -u, --username USERNAME          Login with this account ID
# -p, --password PASSWORD          Account password. If this option is left out, youtube-dl will ask interactively.

# Subtitle options
# "--write-sub",  # Write subtitle file
# "--write-auto-sub",  # Write automatically generated subtitle file (YouTube only)
# --sub-lang LANGS Languages of the subtitles to download (optional) separated by commas, use IETF language tags like 'en,pt'

class Youtubedl:
    # generic_options = [
    #     "-q"  # Activate quiet mode
    # ]

    # general_opions = [
    #     "-i"  # Continue on download errors, for example to skip unavailable videos in a playlist
    # ]

    filesystem_options = [
        "--cookies"  # File to read cookies from and dump cookie jar in
    ]

    verbosity_options = [
        "-g",  # Simulate, quiet but print URL
    ]

    # video_format_options = [
    #     "-F",  # List all available formats of specified videos
    #     "--youtube-skip-dash-manifest"  # Do not download the DASH manifests and related data on YouTube videos
    # ]

    cookie = [COOKIE_FILE]
    name = ["youtube-dl"]
    youtube_url = None

    # raw_available_formats = []
    # mp4_options = []
    # best_format_code = None

    def __init__(self, youtube_url):
        self.youtube_url = [youtube_url]
        # self.__get_available_formats(self.youtube_url)
        # self.__get_mp4_options(self.raw_available_formats)
        # self.__get_best_format(self.mp4_options)

    # def __get_available_formats(self, youtube_url):
    #     try:
    #         command = self.name + self.video_format_options + self.youtube_url
    #
    #         print_info("getting available formats...")
    #
    #         p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    #                              shell=False)
    #         p.wait()
    #
    #         output, error = p.communicate()
    #
    #         if not error:
    #             self.raw_available_formats = output
    #         else:
    #             handle_error(error)
    #     except Exception as e:
    #         handle_exception(e)

    # def __get_mp4_options(self, raw_available_formats):
    #     mp4 = re.compile("(\s*[0-9]*\s*mp4\s*[0-9]{3,4}x[0-9]{3,4}\s*(?!\s*.*DASH.*)\w*.*)")
    #     mp4_options = []
    #
    #     for frmt in raw_available_formats.split(b"\n"):
    #         match = mp4.match(frmt.decode("UTF-8"))
    #         if match:
    #             print(match.group(0))
    #             mp4_options.append(frmt.decode("UTF-8"))
    #
    #     if mp4_options:
    #         self.mp4_options = mp4_options
    #     else:
    #         handle_error("No matching mp4 videos found")

    # def __get_best_format(self, formats):
    #     best_format = None
    #
    #     for frmt in formats:
    #         if "best" in frmt.lower():
    #             best_format = frmt
    #         else:
    #             best_format = formats[-1]
    #
    #     if best_format:
    #         self.best_format_code = best_format.split()[0]
    #     else:
    #         handle_error("Error retrieving best format")

    def get_url(self):
        try:
            p = subprocess.Popen(self.name + self.filesystem_options + self.cookie + self.verbosity_options +
                                 self.youtube_url, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
            p.wait()

            url, error = p.communicate()

            if error:
                handle_error(error, False)

            if url:
                return "\"{0}\"".format(url.decode(ENCODING).strip())
            else:
                handle_error("Error fetching youtube_url", True)
        except Exception as e:
            handle_exception(e)
