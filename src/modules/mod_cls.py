"""Module to clear the console"""

import os

def cls():
    """Clears the console
    """
    
    # cls on Linux is clear
    os.system("cls" if os.name == "nt" else "clear")