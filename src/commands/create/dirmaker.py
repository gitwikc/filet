import os
from typing import List


def make_file(parent_path: str, filename: str) -> None:
    """
    Creates a file in the given parent path
    with the given filename
    """
    with open(os.path.join(parent_path, filename), 'w') as f:
        f.close()


def make_dir_tree(parent_path: str, tree: List[object], ignored: List[str] = []) -> List[str]:
    """
    Creates a directory tree in the given parent path
    with the given tree and returns the list of files to be ignored
    by git (to be written to a gitignore)
    """
    for i in tree:
        if type(i) == str:
            if i[0] == '*':
                i = i[1:]
                ignored.append(os.path.join(parent_path, i))
            make_file(parent_path, i)
        elif type(i) == dict:
            for folder in i.keys():
                sub_tree = i.get(folder)
                if folder[0] == '*':
                    folder = folder[1:]
                    ignored.append(os.path.join(parent_path, folder))
                os.mkdir(os.path.join(parent_path, folder))
                ignored.append(
                    make_dir_tree(
                        parent_path=os.path.join(parent_path, folder),
                        tree=sub_tree,
                        ignored=ignored))
    return ignored


def create_gitignore(parent_path: str, ignored: List[str]) -> None:
    """
    Creates a .gitignore file for ignoring the given items
    """
    ignored = [line for line in ignored if type(line) is str]

    if ignored:
        with open(os.path.join(parent_path, '.gitignore'), 'w') as f:
            f.writelines(
                [f'{line[len(parent_path):]}\n'.replace('\\', '/').lstrip('/') for line in ignored if type(line) is str])
            f.close()
