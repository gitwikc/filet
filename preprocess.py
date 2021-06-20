import argparse


def get_args() -> argparse.Namespace:
    """
    Gets the command line arguments
    """
    ap = argparse.ArgumentParser()

    ap.add_argument('--root', '-r', type=str,
                    nargs='?', default='.',
                    required=False,
                    help='Location of root directory to create the filetree')
    ap.add_argument('struc', type=str,
                    help='The structure of the filetree in filet syntax')
    ap.add_argument('--notree',
                    action='store_true',
                    help='File tree will not be logged to console')
    args = ap.parse_args()
    return args
