from colorama import Fore


def get_release_info():
    return {
        "version": "1.8.0",
        "date": "2022-02-11"
    }


def print_version_info():
    release_info = get_release_info()
    print(
            f"> Filet version\t\t{Fore.YELLOW}{release_info['version']}{Fore.RESET}")
    print(
            f"> Release date\t\t{Fore.MAGENTA}{release_info['date']}{Fore.RESET}\n{'-' * 40}")
