from preprocess import get_tree
import sys
from pprint import pprint


def main():
    pass


if __name__ == "__main__":
    arg = sys.argv[1]
    print(arg)
    pprint(get_tree(arg))
