from requests import get
import subprocess
import os
from util.version import get_release_info
from halo import Halo
from colorama import init as colorama_init, Fore

colorama_init(autoreset=True)


def get_releases_list():
    req = get('https://api.github.com/repos/gitwikc/filet/releases')
    release_data = req.json()
    releases = []
    for release in release_data:
        releases.append({
            'name': release['tag_name'],
            'prerelease': release['prerelease'],
            'published_at': release['published_at'],
            'download_url': release['assets'][0]['browser_download_url']
        })
    releases.sort(key=lambda x: x['published_at'], reverse=True)
    return releases


def get_available_update():
    latest_release = get_releases_list()[0]
    current_release = get_release_info()
    if latest_release['name'] != current_release['version']:
        return latest_release
    else:
        return None


def download_filet(download_url: str, dest: str):
    spinner = Halo(text='Downloading update', spinner='dots')
    spinner.start()
    req = get(download_url)
    spinner.stop()
    print(f'{Fore.LIGHTGREEN_EX}\u2714 {Fore.RESET}Download complete')
    print('Writing to file...')
    with open(dest, 'wb') as f:
        f.write(req.content)
        print(f'{Fore.LIGHTGREEN_EX}Done')
        f.close()
    spinner.stop()
    print(f'{Fore.LIGHTBLUE_EX}Starting installer...')
    return subprocess.call([dest])


def check_for_updates(verbose: bool = False):
    if verbose:
        spinner = Halo(text='Checking for updates...', spinner='dots')
        spinner.start()
    latest_update = get_available_update()
    if verbose:
        spinner.stop()

    if latest_update and not latest_update['prerelease']:
        print(
            f"An update to version {Fore.LIGHTYELLOW_EX}{latest_update['name']}{Fore.RESET} is available. Do you want to install it? (y/n)")
        print(f"{Fore.LIGHTCYAN_EX}>> {Fore.RESET}", end='')
        if input().lower() == 'y':
            installer_filename = f'filet_{latest_update["name"]}.exe'
            download_filet(
                download_url=latest_update['download_url'],
                dest=installer_filename)
            os.remove(installer_filename)
    elif verbose:
        print('> Filet is up-to-date. No updates available <')


if __name__ == '__main__':
    latest_update = get_available_update()
    if latest_update:
        print(
            f"Update available: {latest_update['name']} ({latest_update['published_at']})")
    else:
        print('Filet is up to date')
