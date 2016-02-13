"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    exception_handler  
"""

from crosscutting.condition_messages import print_exception


def handle_exception(e):
    print_exception(e)
    exit(2)
