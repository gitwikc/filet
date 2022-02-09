import os
from pathlib import Path
from typing import Dict


def get_tree_at_location(root, depth: int = 0, max_depth: int = None) -> Dict:
    """
    Gets the tree of a directory as a dict
    that can be printed by print_tree()

    :param root: Directory whose tree required
    :param max_depth: Max depth into the tree reached by the crawler.
    For example, max_depth=2 would mean the deepest item in the dict
    would correspond to something like 'dir1/dir2/file.txt'
    :param depth: Internal state in recursive function storing current depth
    """
    filetree = []
    children = os.listdir(Path(root))
    children_paths = [Path(os.path.join(root, child)) for child in children]
    for child, child_path in zip(children, children_paths):
        if child_path.is_file():
            filetree.append(child)
        elif child_path.is_dir():
            value = get_tree_at_location(child_path, depth + 1, max_depth) \
                if (max_depth is None or depth < max_depth) else []
            filetree.append({child: value})
    return filetree
