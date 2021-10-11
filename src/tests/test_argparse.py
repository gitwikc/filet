import argparse
from pprint import pprint

ap = argparse.ArgumentParser()

ap.add_argument('--root', '-r', type=str,
                nargs='?', default='.',
                required=False, help='Root directory to create the filetree')
ap.add_argument('struc', type=str,
                help='The structure of the filetree in filet synax')
ap.add_argument('--notree',
                action='store_true',
                help='File tree will not be logged to console')
args = vars(ap.parse_args())

pprint(args)
