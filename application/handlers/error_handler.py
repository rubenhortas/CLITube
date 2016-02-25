"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    error_handler  
"""

from crosscutting.condition_messages import print_error
from crosscutting.condition_messages import print_warning
from crosscutting.constants import ENCODING


def handle_error(error, ext):
    if error.split()[0] == b"WARNING:":
        print_warning(error.replace(b"WARNING:", "").strip())
    elif error.split()[0] == b"ERROR:":
        print_error(error.replace(b"ERROR:", "").strip())
    else:
        print(error)

    if ext:
        exit(1)
