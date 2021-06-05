from dirmaker import make_dir_tree
from preprocess import get_tree
import sys
from pprint import pprint


def main():
    pass


if __name__ == "__main__":
    parent_path, arg = sys.argv[1:3]
    print(parent_path, arg)
    make_dir_tree(parent_path, get_tree(arg))
