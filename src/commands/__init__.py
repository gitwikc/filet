from argparse import _SubParsersAction, ArgumentParser
from typing import Dict, List


class Subcommand:
    """
    Creates a subcommand and adds it to the given subparsers

    :param command_name: The command name
    :param subparsers: The subparsers to add the subcommand to
    :param help: Help message for the subcommand
    :param subcommand_classes: The list of subcommand classes; These classes inherit Subcommand
    """
    def __init__(
        self, command_name: str,
        subparsers: _SubParsersAction,
        help: str = 'Sub command',
        subcommand_classes: List = []) -> None:
        self.command_name = command_name
        self.parser: ArgumentParser = subparsers.add_parser(self.command_name, help=help)
        if len(subcommand_classes) > 0:
            self.sub_parsers = self.parser.add_subparsers(
                title=f'Sub commands for {self.command_name}', dest=self.command_name)
            self.subcommands: List[Subcommand] = [
                subcommand_class(self.sub_parsers)
                for subcommand_class in subcommand_classes]
        self._add_arguments()

    def _add_arguments(self):
        """
        Adds arguments to the subcommand
        """
        pass

    def call(self, args: Dict):
        """
        Calls the subcommand with the given args. The action to be taken
        with the args is declared inside this method

        :param args: Dict obtained by vars() on result of parse_args()
        """
        for subcommand in self.subcommands:
            if args[self.command_name] == subcommand.command_name:
                subcommand.call(args)
