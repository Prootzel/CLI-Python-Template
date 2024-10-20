"""Help module"""

from typing import Final
import json

from src.lib.printer import p as print

# load command list for full help command list
CMD_LIST_PATH = "src/static/help/_command_list.json"
with open(CMD_LIST_PATH, "r") as file:
    COMMANDS : Final = json.load(file)

def handle_help(string : str):
    """Handle an incoming help command

    Args:
        string (str): Full help command
    """
    if(len(string.split(" ")) > 1):
        if(string[1].lower() == "python"):
            print_help_python()
        else:
            print_help_command(string.split(" ")[1])
    else:
        print_help()

def print_help_python():
    """Get official python help text"""
    print(help())

def print_help():
    """Print all commands"""
    for command in COMMANDS.keys():
        print(f"{command}", fore_color = "cyan", end = " ")
        print(f": {COMMANDS[command]}")
        
def print_help_command(command : str):
    """Print full help on command

    Args:
        command (str): 
    """
    try:
        with open(f"src/static/help/{command}.txt", "r") as file:
            print(command, fore_color="cyan")
            print("--------------------")
            print(file.read())
    except FileNotFoundError:
        print("Help file not found; does this command exist?")