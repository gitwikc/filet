import os


def make_file(parent_path: str, filename: str) -> None:
    with open(f"{parent_path}/{filename}", 'w') as f:
        f.close()


def make_dir_tree(parent_path: str, tree: list) -> None:
    for i in tree:
        if type(i) == str:
            make_file(parent_path, i)
        elif type(i) == dict:
            for folder in i.keys():
                os.mkdir(f"{parent_path}/{folder}")
                make_dir_tree(
                    parent_path=f"{parent_path}/{folder}", tree=i.get(folder))
