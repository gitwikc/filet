from dirmaker import make_dir_tree
from preprocess import get_args, get_tree
from pprint import pprint


if __name__ == "__main__":
    args = get_args()
    try:
        tree = get_tree(args.struc)
        make_dir_tree(parent_path=args.root, tree=tree)
    except Exception as ex:
        print('An error occured')
        print(ex)
    else:
        print('Successfully created file tree')
        if not args.notree:
            pprint(tree)
