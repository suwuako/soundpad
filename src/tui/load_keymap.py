import os

import src.read_json as read_json

def run():
    """
    :return: keymap path
    """
    while True:
        keymap_path = input("Type in the name of your layout: ")
        true_path = f"{os.path.abspath(os.getcwd())}\data\{keymap_path}.json"

        if os.path.exists(true_path):
            print(f"Loading {keymap_path} at {true_path}")
            input("Press enter to continue")
            return f"data/{keymap_path}.json"
        else:
            print("Invalid input... Try again.")