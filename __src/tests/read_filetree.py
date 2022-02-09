from pathlib import Path
import os
from pprint import pprint
from colorama import init
from src.util.tree import print_tree


root = Path(f"{__file__}/../..")


def list_children(dirname: Path):
    filet_dict = []
    children = os.listdir(Path(dirname))
    children_paths = [Path(os.path.join(dirname, child)) for child in children]
    for child, child_path in zip(children, children_paths):
        if child_path.is_file():
            filet_dict.append(child)
        elif child_path.is_dir():
            filet_dict.append({child: list_children(child_path)})
    return filet_dict

if __name__ == "__main__":
    init()
    mytree = list_children(root)
    pprint(mytree)
    print_tree(mytree)
