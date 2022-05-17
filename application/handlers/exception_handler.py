#!/usr/bin/env python
# _*_ coding:utf-8 _*
from crosscutting.condition_messages import print_exception


def handle_exception(e):
    print_exception(e)
    exit(2)
