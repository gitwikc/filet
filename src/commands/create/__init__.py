from argparse import _SubParsersAction
from typing import Dict
from src.commands import Subcommand
from src.commands.create.dirmaker import create_gitignore, make_dir_tree
from src.util.tree import get_tree, print_tree
from colorama import Fore


class CommandTouch(Subcommand):
    def __init__(self, subparsers: _SubParsersAction) -> None:
        super().__init__('create', subparsers, 'Create file/folder trees')

    def _add_arguments(self):
        # Root directory
        self.parser.add_argument('--root', '-r', type=str,
                                nargs='?', default='.',
                                required=False,
                                help='Location of root directory to create the filetree')

        # File tree structure
        self.parser.add_argument('struc', type=str,
                                help='The structure of the filetree in filet syntax')

        # Print tree after created?
        self.parser.add_argument('--notree',
                                action='store_true',
                                help='File tree will not be logged to console')

    def call(self, args: Dict):
        try:
            tree = get_tree(args['struc'])
            create_gitignore(
                args['root'],
                make_dir_tree(
                    parent_path=args['root'], tree=tree))
        except IndexError as inx_ex:
            print(f'{Fore.RED}Error: Incorrect syntax. Please check filet structure')
        except FileExistsError as fe_ex:
            print(f'{Fore.YELLOW}Warning: File/folder already exists in root directory')
        else:
            print(
                f'{Fore.LIGHTGREEN_EX}\u2714 {Fore.LIGHTWHITE_EX}Successfully created file tree{Fore.RESET}\n')
            if not args['notree']:
                print_tree(tree)
