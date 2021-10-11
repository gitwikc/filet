import subprocess
from src.util.version import get_release_info

version = get_release_info()['version']
subprocess.call(['pyinstaller', 'src/main.py', '--onefile', '--name', 'filet',
                '--icon', 'src/icon/filet.ico', '--distpath', f'dist/executables/{version}', '--clean'])
