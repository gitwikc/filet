from dirmaker import create_gitignore, make_dir_tree
from preprocess import get_args
from util import get_tree, print_tree

from colorama import init as colorama_init, Fore


colorama_init()


if __name__ == "__main__":
    release_info = {
        "version": "v1.7",
        "date": "2021-10-03"
    }
    args = get_args()

    if args.version:
        print(
            f"> Filet version\t\t{Fore.YELLOW}{release_info['version']}{Fore.RESET}")
        print(
            f"> Release date\t\t{Fore.MAGENTA}{release_info['date']}{Fore.RESET}\n{'-' * 40}")

    try:
        tree = get_tree(args.struc)
        create_gitignore(
            args.root,
            make_dir_tree(
                parent_path=args.root, tree=tree))
    except IndexError as inx_ex:
        print(f'{Fore.RED}Error: Incorrect syntax. Please check filet structure')
    except FileExistsError as fe_ex:
        print(f'{Fore.YELLOW}Warning: File/folder already exists in root directory')
    else:
        print(
            f'{Fore.LIGHTGREEN_EX}\u2714 {Fore.LIGHTWHITE_EX}Successfully created file tree{Fore.RESET}\n')
        if not args.notree:
            print_tree(tree)
