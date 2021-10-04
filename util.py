from typing import List
from colorama import init as colorama_init, Fore
from enum import Enum

# Initialize colorama
colorama_init()


class TextColor(Enum):
    FILE = Fore.LIGHTGREEN_EX
    FOLDER = Fore.LIGHTMAGENTA_EX
    IGNORED = Fore.WHITE


def get_tree(arg: str) -> List[object]:
    """
    Creates a file tree from given arg

    :param arg: A string in filet syntax showing the file tree structure
    """
    tree = []
    current_token = ''
    i = 0
    while i < len(arg):
        c = arg[i]
        # Start of folder
        if c == '[':
            # Stores contents of folder
            bracket_content = ''
            # How far into the folder tree are we?
            bracket_depth = 1
            # While still in the folder
            while bracket_depth > 0:
                i += 1
                bracket_content_token = arg[i]

                # Another nested folder?
                if bracket_content_token == '[':
                    bracket_depth += 1  # Go 1 step deeper

                # Folder ends?
                elif bracket_content_token == ']':
                    bracket_depth -= 1  # Come out 1 step

                # Still inside folder?
                if bracket_depth > 0:
                    bracket_content += bracket_content_token

            '''
            Folder contents scanned,
            create subtree now and save under current folder
            '''
            tree.append({current_token: get_tree(bracket_content)})

            # Clear current folder name for next folder/file
            current_token = ''
            i += 1
        elif c == "+" and len(current_token) > 0:
            tree.append(current_token)
            current_token = ''
        elif type(current_token) == str:
            current_token += c
            if i == len(arg) - 1:
                tree.append(current_token)
        i += 1

    return tree


def print_tree(tree, depth: int = 0, prefix_folder: str = chr(31), prefix_file: str = chr(28), ignored: bool = False) -> None:
    """
    Prints the given file tree at the given depth. Depth is the number of levels into the file tree
    at which the control is, currently; this is a recurring function and it is advised not to specify
    the depth unless absolutely sure about the effects.

    :param tree: The tree-like object - a dict, list or string which signifies the file tree or a part of it
    :param depth: The depth of the tree in the file tree (used for indentation)
    :param prefix_folder: The prefix applied to folders in the file tree
    :param prefix_file: The prefix applied to files in the file tree
    :param ignored: Is this tree ignored in `.gitignore`?
    """
    def depth_space():
        """
        Indents the output to the depth in the file tree
        """
        for i in range(depth):
            print(' ' * 4, end='')

    if type(tree) is dict:   # Folder
        for key in tree.keys():
            depth_space()   # Indent

            # Is the folder ignored? Y -> Propagate to children
            ignored |= key.startswith('*')

            # Get text color
            file_text_color = TextColor.IGNORED.value if ignored else TextColor.FOLDER.value
            # Write folder name
            # Removes leading '*'s, if any
            print(f"{prefix_folder} {file_text_color}{key.lstrip('*')}{Fore.RESET}")
            sub_tree = tree.get(key)   # Get folder contents
            # Print folder contents tree
            print_tree(tree=sub_tree, depth=depth+1, ignored=ignored)
    elif type(tree) is list:   # List of files (contents of folder)
        for sub_tree in tree:
            print_tree(tree=sub_tree, depth=depth, ignored=ignored)
    elif type(tree) is str:   # File (tree itself is file name)
        depth_space()

        # Check if file ignored
        ignored |= tree.startswith('*')

        # Get text color
        file_text_color = TextColor.IGNORED.value if ignored else TextColor.FILE.value
        print(f"{prefix_file} {file_text_color}{tree.lstrip('*')}{Fore.RESET}")
