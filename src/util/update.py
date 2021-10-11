from requests import get
from version import get_release_info


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


if __name__ == '__main__':
    latest_update = get_available_update()
    if latest_update:
        print(
            f"Update available: {latest_update['name']} ({latest_update['published_at']})")
    else:
        print('Filet is up to date')
