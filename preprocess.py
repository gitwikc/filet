from typing import List


def get_tree(arg: str) -> List[object]:
    """
    Creates a file tree from given arg
    """
    tree = []
    current_token = ''
    i = 0
    while i < len(arg):
        c = arg[i]
        if c == '[':
            bracket_content = ''
            bracket_depth = 1
            while bracket_depth > 0:
                i += 1
                bracket_content_token = arg[i]
                if bracket_content_token == '[':
                    bracket_depth += 1
                elif bracket_content_token == ']':
                    bracket_depth -= 1
                if bracket_depth > 0:
                    bracket_content += bracket_content_token
            tree.append({current_token: get_tree(bracket_content)})
            current_token = ''
            i += 1
        elif c == "+" and len(current_token) > 0:
            tree.append(current_token)
            current_token = ''
        elif type(current_token) == str:
            current_token += c
            if i == len(arg) - 1:
                tree.append(current_token)
        i += 1

    return tree
