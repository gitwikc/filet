from dirmaker import make_dir_tree
from preprocess import get_args
from util import get_tree, print_tree


if __name__ == "__main__":
    args = get_args()
    try:
        tree = get_tree(args.struc)
        make_dir_tree(parent_path=args.root, tree=tree)
    except IndexError as inx_ex:
        print('Incorrect syntax. Please check filet structure')
    except FileExistsError as fe_ex:
        print('File/folder already exists in root directory')
    except Exception as ex:
        print('An unknown error occured')
    else:
        print('\u2714 Successfully created file tree\n')
        if not args.notree:
            print_tree(tree)
