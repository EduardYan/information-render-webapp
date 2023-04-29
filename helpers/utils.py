"""
This file have some utils functions
for help to the server in process data.

"""

from json import load

def get_json_data(path_file:str) -> dict:
    """
    Open the data file './data.json'
    and return a dict with the data in this file.

    """

    with open(path_file) as f:
        object_content = load(f)

    return object_content

def get_config() -> dict:
    """
    Open the config file './config.json'
    and return a dict with the configuration.

    """

    with open('./config.json') as f:
        content = load(f)

    return content

# global variable
CONFIG = get_config()
