import subprocess
from src.util.version import get_release_info

version = get_release_info()['version']
subprocess.call(['pyinstaller', './src/__main__.py', '--onefile', '--name', 'filet', '--paths', '.',
                '--icon', 'src/icon/filet.ico', '--distpath', f'dist/exe/{version}', '--clean'])
