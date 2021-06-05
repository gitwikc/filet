from dirmaker import make_dir_tree
from preprocess import get_tree
import sys
from pprint import pprint


if __name__ == "__main__":
    parent_path, arg = sys.argv[1:3]
    print(parent_path, arg)

    try:
        tree = get_tree(arg)
        make_dir_tree(parent_path, tree)
    except Exception as ex:
        print('An error occured')
        print(ex)
    else:
        print('Successfully created file tree')
        pprint(tree)
