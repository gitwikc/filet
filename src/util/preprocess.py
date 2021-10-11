import argparse


def get_args() -> argparse.Namespace:
    """
    Gets the command line arguments
    """
    ap = argparse.ArgumentParser()

    info_group = ap.add_argument_group('INFO')
    info_group.add_argument('--version', '-v',
                            action='store_true',
                            help='Prints out current version and release date of Filet')
    info_group.add_argument('--update', '-u',
                            action='store_true',
                            help='Makes the update checker verbose')

    create_group = ap.add_argument_group('CREATE')
    # Root directory
    create_group.add_argument('--root', '-r', type=str,
                              nargs='?', default='.',
                              required=False,
                              help='Location of root directory to create the filetree')

    # File tree structure
    create_group.add_argument('struc', type=str,
                              help='The structure of the filetree in filet syntax')

    # Print tree after created?
    create_group.add_argument('--notree',
                              action='store_true',
                              help='File tree will not be logged to console')
    args = ap.parse_args()
    return args
