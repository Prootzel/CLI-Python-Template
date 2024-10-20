"""Module for unknown commands"""

from src.lib.printer import p as print

def print_unknown():
    """Print this if a command was not found"""
    print("Unknown command", fore_color="red")