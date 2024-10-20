"""Holder for keys if required"""
from typing import Final
API_KEY : str 
CLIENT_SECRET : str

with open("keys/api.key", "r") as key:
    API_KEY : Final = key.read()
    
with open("keys/client_secret.key", "r") as key:
    CLIENT_SECRET : Final = key.read()