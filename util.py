from typing import List


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


def print_tree(tree, depth: int = 0, prefix_folder: str = chr(31), prefix_file: str = chr(28)) -> None:
    """
    Prints the given file tree at the given depth. Depth is the number of levels into the file tree
    at which the control is, currently; this is a recurring function and it is advised not to specify
    the depth unless absolutely sure about the effects.

    :param tree: The tree-like object - a dict, list or string which signifies the file tree or a part of it
    :param depth: The depth of the tree in the file tree (used for indentation)
    :param prefix_folder: The prefix applied to folders in the file tree
    :param prefix_file: The prefix applied to files in the file tree
    """
    def depth_space():
        """
        Indents the output to the depth in the file tree
        """
        for i in range(depth):
            print('    ', end='')

    if type(tree) is dict:   # Folder
        for key in tree.keys():
            depth_space()   # Indent
            print(f"{prefix_folder} {key}")   # Write folder name
            sub_tree = tree.get(key)   # Get folder contents
            print_tree(sub_tree, depth=depth+1)  # Print folder contents tree
    elif type(tree) is list:   # List of files (contents of folder)
        for sub_tree in tree:
            print_tree(sub_tree, depth=depth)
    elif type(tree) is str:   # File
        depth_space()
        print(f"{prefix_file} {tree}")
