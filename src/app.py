"""Main Application file
This runs the main loop and parses commands
"""

from sys import exit
import importlib

from imports.printer_imports import *
from imports.module_imports import *

def parse_command(command : str):
    """Parse a command

    Args:
        command (str)
    """
    if(len(command.split(" ")) > 1):
        root = command.split(" ")[0]
    else:
        root = command
    
    log.info(command)    
    
    match root:
        case "exit":
            exit()
        case "help":
            mod_help.handle_help(command)
        case "cls"|"clear":
            mod_cls.cls()
        case "reload":
            print("Reloading all modules...")
            try:
                importlib.reload(mod_cls)
                importlib.reload(mod_requests)
                importlib.reload(mod_help)
                importlib.reload(mod_unknown_command)
            except Exception as e:
                log.error(f"Exception when reloading: {e}")
                print(f"Exception when reloading: {e}", fore_color="red")
            else:
                print("Done", fore_color="cyan")
            
        case "get" | "post":
            try:
                pprint(mod_requests.handle_command(command))
            except Exception as e:
                print(f"Exception when trying to use {command.split(" ")[0].lower()}: {e}")
            
        case _:
            mod_unknown_command.print_unknown()
            
def loop():
    """Run the main loop"""
    while True:
        try:
            print(">", fore_color="green", end = " ")
            parse_command(input())
        except KeyboardInterrupt:
            print("Keyboard interrupt, exiting...", fore_color="red")
            log.info("Keyboard interrupt, exiting...")
            
            exit()


def start():
    """Start execution"""
    loop()