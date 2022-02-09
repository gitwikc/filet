from argparse import _SubParsersAction
from typing import Dict
from src.commands.peek.crawler import get_tree_at_location
from src.commands import Subcommand
from src.util.tree import print_tree


class CommandPeek(Subcommand):
    def __init__(self, subparsers: _SubParsersAction) -> None:
        super().__init__('peek', subparsers, 'Shows the tree of the given directory')

    def _add_arguments(self):
        self.parser.add_argument('--root', '-r', type=str, default='.', help='Location of directory')
        self.parser.add_argument('--max-depth', '-d', type=int, help='Max depth to which tree is seen')

    def call(self, args: Dict):
        root = args['root']
        max_depth = args['max_depth']
        print_tree(get_tree_at_location(root, max_depth=max_depth))
