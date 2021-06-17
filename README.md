# Filet
The ⚡ superfast ⚡ CLI tool to create file trees at the drop of a hat

## Installation 📥
1. Download `filet.exe` from the [releases](https://github.com/gitwikc/filet/releases) page
2. Add the path of the folder where you stored `filet.exe` to the system **PATH** variable like [this](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho)
3. Restart your computer and Filet is ready to be used in your favorite terminal! 🥳🎆

## Usage :electric_plug: 💻
Use the `--help` flag for instructions
```
$ filet --help
usage: filet.exe [-h] [--root [ROOT]] [--notree] struc

positional arguments:
  struc                 The structure of the filetree in filet synax

optional arguments:
  -h, --help            show this help message and exit
  --root [ROOT], -r [ROOT]
                        Root directory to create the filetree
  --notree              File tree will not be logged to console
```
### Syntax 👩‍🏫
| item   | syntax                                              | example1                         | example2            |
|--------|-----------------------------------------------------|----------------------------------|---------------------|
| file   | `{file_name1}.{extension}+{file_name2}.{extension}` | `hello.py`                       | `server.js+auth.js` |
| folder | `{folder_name1}[]+{folder_name2}[]`                 | `src[]`                          | `api[]+auth[]`      |
| tree   | `{folder_name}[{file1}+{file2}+...]`                | `src[main.jsx+data[users.json]]` |                     |

### Example 🥊
1. Create file tree in current directory
```
$ filet dir1[f1.txt+f2.txt+dir2[f3.txt]]
Successfully created file tree
[{'dir1': ['f1.txt', 'f2.txt', {'dir2': ['f3.txt']}]}]
```
2. Create file tree in specified directory using `-r` or `--root` arg

- **Absolute path**
`$ filet -r C://Users//ADMIN myfolder[images[]+important[bday.txt+todos.txt]]+software[README.txt]`<br />
Creates file tree in `C://Users//ADMIN` directory

- **Relative path**
`$ filet ../tests myfolder[images[]+important[bday.txt+todos.txt]]+software[README.txt]`<br />
Creates the file tree in the parent directory of current directory (in which the terminal runs `filet` command)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
