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
    msg = error.decode("UTF-8")

    if msg.split()[0] == "WARNING:":
        print_warning(msg.replace("WARNING:", "").strip())
    elif msg.split[0] == "ERROR:":
        print_error(msg.replace("ERROR:", "").strip())
    else:
        print(msg)

    if ext:
        exit(1)
