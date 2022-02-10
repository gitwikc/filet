from argparse import _SubParsersAction
from typing import Dict
from src.commands import Subcommand
from src.commands.update.updater import check_for_updates


class CommandUpdate(Subcommand):
    def __init__(self, subparsers: _SubParsersAction) -> None:
        super().__init__('update', subparsers, 'Check for updates')

    def _add_arguments(self):
        self.parser.add_argument('--silent', '-s', action='store_true', help='Makes updates non verbose')

    def call(self, args: Dict):
        check_for_updates(verbose=(not args['silent']))
