from argparse import ArgumentParser
from colorama import init, Fore, Back, Cursor

init()

argp = ArgumentParser(
    prog='filet',
    description=f'Superfast CLI to create {Fore.YELLOW}filetrees{Fore.RESET}'
)

argp.add_argument('--version', '-v', action='store_true', dest='version')

subparser = argp.add_subparsers(title='filet', dest='main', description='Parser for sub commands')

touchparser = subparser.add_parser('touch', help='Create filetree')
touchparser.add_argument('struc', help='Filet syntax for filetree')
touchparser.add_argument('--root', '-r', type=str, help='Root directory to create the filetree')

viewparser = subparser.add_parser('peek', help='View file structure of existing directory')
viewparser.add_argument('root', type=str, help='Root from which filetree is to be viewed')

editparser = subparser.add_parser('edit', help='Edit existing filetree')
editsubparser = editparser.add_subparsers(
    dest='edit',
    description='Sub commands for edit',
    required=True)
edit_cutparser = editsubparser.add_parser('cut', help='Cut an item')
edit_cutparser.add_argument('itempath', help='Path of item to cut')
edit_copyparser = editsubparser.add_parser('copy')
edit_copyparser.add_argument('itempath', help='Path of item to copy')

args = argp.parse_args()
print(vars(args))
if args.main is None and args.version:
    print('v1.7')

