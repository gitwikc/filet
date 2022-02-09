from argparse import ArgumentParser

from src.commands.touch import CommandTouch
from src.commands.peek import CommandPeek
from src.commands.update import CommandUpdate


main_parser = ArgumentParser(
    prog='filet',
    description='The helpful CLI')
subparsers = main_parser.add_subparsers(
    dest='main',
    title='Sub Commands',
    description='Sub commands for the CLI',
)

# calc subcommand
subcommands = {
    'touch': CommandTouch(subparsers),
    'peek': CommandPeek(subparsers),
    'update': CommandUpdate(subparsers)
}


def call():
    args = vars(main_parser.parse_args())
    subcommands[args['main']].call(args)
    # Do whatver else you want to with the args, here
