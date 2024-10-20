# The python CLI Template

## About
This is a template made in Python 3.13. It is supposed to aid in gettings basic thing like help menus done quickly.

## First start

First, download the repository. You can do so with the following command if you have git installed. If not, just use the download button in the top right corner and extract the zip file.

```git clone https://github.com/Prootzel/CLI-Python-Template```

Make sure you have python installed. If so, create a virtual environment. Use a folder name you can remember for it.

```python -m venv ./[folder name]```

Now enter it. Try the other activation scripts if this one doesn't work.
```./[folder name]/Scripts/activate```

Then, install the required modules. They are bundled in requirements.txt.

```pip install -r requirements.txt```

Lastly, launch starter.py.
```python starter.py```

You should see a green arrow appear.

## Concept
The program classifies files in 3 different categories, library, modules and static.

1. **Library**
Library files are **global** files with **executable code** that serve a **generic purpose**.

2. **Modules**
Modules are **non-global** files with **executable code** that serve a **specific purpose**.

3. **Static**
Static files are **global** files with **no executable code** except for setup. They can be script files with only variables however.

There is also imports, which purely serve to ease importing of multiple files, keys, which store API keys and similar, and logs, which store logs on execution.

### Examples:
1. printer.py (Library)
2. mod_cls.py (Module)
3. ansi_codes.py (Static)

## Naming conventions

### Modules
Modules always start with a `mod_`.

### Colors and Styling for printer.py
Available ANSI colors are "black", "white", "blue", "yellow", "cyan", "green", "red", "clear". Available ANSI stylings are "bold", "underline", "reverse", "". An empty string clears the styling.

### Keys
Keys have the `.key` file extension.

### Logs
Logs have the `.log` file extension.

### Help texts
Help texts have the `.txt` file extension. They are titled after the lowercase of their respective command. They start with an explanation of the command, proceeded by any number of the following (seperated by 1 empty line each) if wanted:

1. Required arguments
First write "Required Arguments".
Add an indent of 4 (1 tab) before any required arguments. For user input, surround it in square brackets. Have an indent of at least 8 (2 tabs) minus the argument length after. Explain the argument here. All argument explanations should be at the same level of indentation.

2. Optional arguments
First write "Optional Arguments".
Add an indent of 4 (1 tab) before any optional arguments. For user input, surround it in square brackets. Have an indent of at least 8 (2 tabs) minus the argument length after. Explain the argument here. All argument explanations should be at the same level of indentation.

2. Examples
First write "Examples".
Add an indent of 4 (1 tab). Then, write an example command. If you want, put an explanation in the line(s) below.

## Included commands

### clear
Clears the command line.

### cls
Alternative to clear.

### exit
Exit the CLI.

### get [target]
Send a get request to the target.

### help
Get a summary of all commands

### help [command]
Get a long explanation of that command.

### post [target] [data]
Send a post request to the target with data. Likely very broken.

### reload
Reload all modules.
This command is not part of a module itself.

## Folder structure and explanation

The folder structure is as follows:
```
template/               
├─ keys/                
├─ logs/                
├─ src/                 
│  ├─ imports/       
│  ├─ lib/
│  ├─ modules/
│  ├─ static/
│  │  ├─ help/
```
### keys
Folder to store files containing API keys and such.

### logs
Folder to store logs.

### src
Source folder containing code and libraries

#### imports
Simple import files to make importing groups of python files using wildcard imports easier. Example: All print-related functions, all modules.

#### lib
Library folder. Libraries are, for this project, globally accessed packages and functions that can run code.

#### modules
Modules folder. Modules are parts handling certain commands of a program. Some modules can rely on other modules. Included by default are a module to clear the screen, a help command module, a simple HTTP request module and a module to process unknown commands.

#### static
Folder for non-code files containing data.

##### help
Folder containing all the help files. _command_list.json stores all commands with a short description while each command gets its own .txt long explanation file.

## Full file structure and file explanation

```template/
├─ keys/
│  ├─ api.key
│  ├─ client_secret.key
├─ logs/
├─ src/
│  ├─ imports/
│  │  ├─ module_imports.py
│  │  ├─ printer_imports.py
│  ├─ lib/
│  │  ├─ printer.py
│  ├─ modules/
│  │  ├─ mod_cls.py
│  │  ├─ mod_help.py
│  │  ├─ mod_requests.py
│  │  ├─ mod_unknown_command.py
│  ├─ static/
│  │  ├─ help/
│  │  │  ├─ _command_list.json
│  │  │  ├─ cls.txt
│  │  │  ├─ clear.txt
│  │  │  ├─ exit.txt
│  │  │  ├─ get.txt
│  │  │  ├─ help.txt
│  │  │  ├─ post.txt
│  │  │  ├─ reload.txt
│  │  ├─ ansi_codes.py
│  ├─ app.py
│  ├─ client_holder.py
│  ├─ keys.py
├─ starter.py
├─ README.md
```

## *.key
Default file format for key files.

## *.log
Default file format for log files.

## starter.py
Starting file. It's chosen as it lies above the src folder, making access to e.g. the keys folder easier.

## printer.py
Print and log handler with color support.

## module_imports.py
Import all modules by using
```py
from src.imports.module_imports import *
```

## printer_imports.py
Import all printer by using
```py
from src.imports.printer_imports import *
```
!WARNING! This overrides python's native print function by default. If you wish to change that, edit the file and change 
```py 
from src.lib.printer import p as print
```
to
```py 
from src.lib.printer import p as [your function name]
```