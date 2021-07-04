<p align="center">
    <img src="./img/filet.png">
</p>

# Filet

The ⚡ superfast ⚡ CLI tool to create file trees at the drop of a hat

## Installation 📥

> If you already have `filet` installed on your computer, you may want to [update](#updating) to the latest version.

1. Download (latest or desired version) `filet.exe` from the [releases](https://github.com/gitwikc/filet/releases) page
2. Add the path of the folder where you stored `filet.exe` to the system **PATH** variable like [this](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho)
3. (_Optional_) Restart your computer and Filet is ready to be used in your favorite terminal! 🥳🎆

## Usage :electric_plug: 💻

Use the `--help` flag for instructions

```
$ filet --help
usage: filet.exe [-h] [--version] [--root [ROOT]] [--notree] struc

optional arguments:
  -h, --help            show this help message and exit

INFO:
  --version, -v         Prints out current version and release date of Filet

CREATE:
  --root [ROOT], -r [ROOT]
                        Location of root directory to create the filetree
  struc                 The structure of the filetree in filet syntax
  --notree              File tree will not be logged to console
```

### Syntax 👩‍🏫

| item   | syntax                                              | example1                         | example2            |
| ------ | --------------------------------------------------- | -------------------------------- | ------------------- |
| file   | `{file_name1}.{extension}+{file_name2}.{extension}` | `hello.py`                       | `server.js+auth.js` |
| folder | `{folder_name1}[]+{folder_name2}[]`                 | `src[]`                          | `api[]+auth[]`      |
| tree   | `{folder_name}[{file1}+{file2}+...]`                | `src[main.jsx+data[users.json]]` |                     |

### Example 🥊

1. Create file tree in current directory

```
$ filet dir1[f1.txt+f2.txt+dir2[f3.txt]]
✔ Successfully created file tree

▼ dir1
    ∟ f1.txt
    ∟ f2.txt
    ▼ dir2
        ∟ f3.txt
```

2. Create file tree in specified directory using `-r` or `--root` arg

- **Absolute path**<br />
  `$ filet -r C://Users//ADMIN myfolder[images[]+important[bday.txt+todos.txt]]+software[README.txt]`<br />
  Creates file tree in `C://Users//ADMIN` directory

- **Relative path**<br />
  `$ filet --root ../tests myfolder[images[]+important[bday.txt+todos.txt]]+software[README.txt]`<br />
  Creates the file tree in the `tests` folder in **parent directory** of current directory (in which the terminal runs `filet` command)

## Updating

To update the version of `filet` on your computer:

1. Download the desired (preferably _latest_) version of `filet.exe` from the [releases](https://github.com/gitwikc/filet/releases) page.
2. Save it in the directory where you have previously installed `filet`
3. :party_popper: YAY! You have successfully updated `filet` on your computer

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[ISC](https://choosealicense.com/licenses/isc/)
