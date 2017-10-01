# -*- coding: utf-8 -*-

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    clitube_messages  
"""

from .condition_messages import print_info


def print_header():
    print_info("CLITube\n")


def print_fetching(video):
    print_info("Fetching: {0}".format(video))
