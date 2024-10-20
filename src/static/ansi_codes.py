"""File to hold all required ansi codes for the terminal
"""

from typing import Final

CLEAR : Final = "\033[00m"

BLACK_FORE : Final = "\033[30m"
BLACK_BACK : Final = "\033[40m"

RED_FORE : Final = "\033[91m"
RED_BACK : Final = "\033[101m"

GREEN_FORE : Final = "\033[92m"
GREEN_BACK : Final = "\033[102m"

YELLOW_FORE : Final = "\033[93m"
YELLOW_BACK : Final = "\033[103m"

BLUE_FORE : Final = "\033[94m"
BLUE_BACK : Final = "\033[104m"

CYAN_FORE : Final = "\033[96m"
CYAN_BACK : Final = "\033[106m"

WHITE_FORE : Final = "\033[97m"
WHITE_BACK : Final = "\033[107m"

BOLD : Final = "\033[1m"
UNDERLINE : Final = "\033[4m"
REVERSE : Final = "\033[7m"