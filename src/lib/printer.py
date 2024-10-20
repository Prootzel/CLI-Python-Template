"""Custom print commands"""

from pprint import pprint
from src.static import ansi_codes
import logging
from datetime import datetime

# configure and initiate logger
LOG_FORMAT = '[%(asctime)s] (%(levelname)s): %(message)s'
logging.basicConfig(filename=f"logs/{datetime.now().strftime("%Y_%m_%d-%H_%M_%S")}.log", level = logging.INFO, format=LOG_FORMAT,  datefmt='%m/%d/%Y %I:%M:%S %p')
LOGGER = logging.getLogger()

def p(string : str, fore_color : str = "clear", back_color : str = "clear", style : str = "", end : str = "\n", sep : str = ","):
    """Custom print function with color support

    Args:
        string (str): String to print
        fore_color (str, optional): One of ["black", "white", "blue", "yellow", "cyan", "green", "red", "clear"]. Defaults to "clear".
        back_color (str, optional): One of ["black", "white", "blue", "yellow", "cyan", "green", "red", "clear"]. Defaults to "clear".
        style (str, optional): One of ["bold", "underline", "reverse", ""]. Defaults to "".
        end (str, optional): Lineends (like in the default print function). Defaults to "\\n".
        sep (str, optional): Element seperators (like in the default print function). Defaults to ",".
    """
    fore_color, back_color, style = fore_color.lower(), back_color.lower(), style.lower()
    
    match style:
        case "bold":
            print(ansi_codes.BOLD, end="")
        case "underline":
            print(ansi_codes.UNDERLINE, end="")
        case "reverse":
            print(ansi_codes.REVERSE, end="")
            
        case _:
            ...
    
    match fore_color:
        case "black":
            print(ansi_codes.BLACK_FORE, end="")
        case "white":
            print(ansi_codes.WHITE_FORE, end="")
        case "blue":
            print(ansi_codes.BLUE_FORE, end="")
        case "yellow":
            print(ansi_codes.YELLOW_FORE, end="")
        case "cyan":
            print(ansi_codes.CYAN_FORE, end="")
        case "green":
            print(ansi_codes.GREEN_FORE, end="")
        case "red":
            print(ansi_codes.RED_FORE, end="")
            
        case "clear"|_:
            ...
            
    match back_color:
        case "black":
            print(ansi_codes.BLACK_BACK, end="")
        case "white":
            print(ansi_codes.WHITE_BACK, end="")
        case "blue":
            print(ansi_codes.BLUE_BACK, end="")
        case "yellow":
            print(ansi_codes.YELLOW_BACK, end="")
        case "cyan":
            print(ansi_codes.CYAN_BACK, end="")
        case "green":
            print(ansi_codes.GREEN_BACK, end="")
        case "red":
            print(ansi_codes.RED_BACK, end="")
            
        case "clear"|_:
            ...

    print(string, end = end, sep = sep)
    print(ansi_codes.CLEAR, end="")

def pp(string : str):
    """pprint wrapper

    Args:
        string (str)
    """
    pprint(string, indent=4, underscore_numbers=True)

def clear():
    """Clear all styling options"""
    print(ansi_codes.CLEAR, end="")

def lb():
    """Print a linebreak"""
    print()