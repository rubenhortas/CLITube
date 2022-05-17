#!/usr/bin/env python
# _*_ coding:utf-8 _*
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
