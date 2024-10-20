"""Simple HTTP request module"""

import requests

def handle_command(command : str) -> requests.Response:
    """Handle incoming GET/POST command requests

    Args:
        command (str): Full command

    Raises:
        Exception

    Returns:
        str: Full response if successfull
    """
    command = command.split(" ")
    if(len(command) != 2):
        raise Exception("Command does not have a target URL/too many arguments")
    else:
        if(command[0].lower() == "post"):
            return post(command[1], command[2])
        elif(command[0].lower() == "get"):
            return get(command[1])
        
def get(url : str, headers : str | None = None, data : str | None = None) -> requests.Response:
    """HTTP Get Handler"""
    return requests.get(url, headers = headers, data = data)

def post(url, data, headers : str | None = None) -> requests.Response:
    """HTTP Post Handler"""
    return requests.post(url, headers = headers, data = data)