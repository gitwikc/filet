from dirmaker import create_gitignore, make_dir_tree
from preprocess import get_args
from util import get_tree, print_tree


if __name__ == "__main__":
    release_info = {
        "version": "v1.5",
        "date": "2021-07-04"
    }
    args = get_args()

    if args.version:
        print(
            f"> Filet version\t\t{release_info['version']}\n> Release date\t\t{release_info['date']}\n{'-' * 40}")

    try:
        tree = get_tree(args.struc)
        create_gitignore(
            args.root,
            make_dir_tree(
                parent_path=args.root, tree=tree))
    except IndexError as inx_ex:
        print('Incorrect syntax. Please check filet structure')
    except FileExistsError as fe_ex:
        print('File/folder already exists in root directory')
    else:
        print('\u2714 Successfully created file tree\n')
        if not args.notree:
            print_tree(tree)
