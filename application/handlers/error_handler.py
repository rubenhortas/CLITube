#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    error_handler  
"""

from crosscutting.condition_messages import print_error
from crosscutting.condition_messages import print_warning


def handle_error(error, ext):
    if error.split()[0] == "WARNING:":
        if "outdated" in error:
            ext = True
        print_warning(error.replace("WARNING:", "").strip())
    elif error.split()[0] == "ERROR:":
        print_error(error.replace("ERROR:", "").strip())
    else:
        print(error)

    if ext:
        exit(1)
