from .condition_messages import print_info


def print_header():
    print_info("CLITube\n")


def print_fetching(video):
    print_info("Fetching: {0}".format(video))
