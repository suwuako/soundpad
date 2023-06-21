import os

import src.read_json as read_json

from colorama import Fore, Back, Style, init


def run():
    """
    :return: keymap path
    """
    init(autoreset=True)
    while True:
        keymap_path = input("Type in the name of your layout: ")
        true_path = f"{os.path.abspath(os.getcwd())}\data\{keymap_path}.json"

        if os.path.exists(true_path):
            print(f"Loading {keymap_path} at {true_path}")
            input(f"{Fore.GREEN} Done! Press enter to continue")
            return f"data/{keymap_path}.json"
        else:
            print(f"{Fore.RED} Invalid input... Try again.")