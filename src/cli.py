from argparse import ArgumentParser
from colorama import Fore

from src.util.version import get_release_info

from src.commands.create import CommandTouch
from src.commands.peek import CommandPeek
from src.commands.update import CommandUpdate


main_parser = ArgumentParser(
    prog='filet',
    description='CLI for the filetree planters out there')

main_parser.add_argument('--version', '-v', action='store_true', default=False, help='Shows version info')

subparsers = main_parser.add_subparsers(
    dest='main',
    title='Sub Commands',
    description='Use these subcommands to perform multiple tasks',
)

# calc subcommand
subcommands = {
    'create': CommandTouch(subparsers),
    'peek': CommandPeek(subparsers),
    'update': CommandUpdate(subparsers)
}


def call():
    args = vars(main_parser.parse_args())
    if args['version']:
        release_info = get_release_info()
        print(
            f"> Filet version\t\t{Fore.YELLOW}{release_info['version']}{Fore.RESET}")
        print(
            f"> Release date\t\t{Fore.MAGENTA}{release_info['date']}{Fore.RESET}\n{'-' * 40}")

    if args['main']:
        subcommands[args['main']].call(args)
