import os

import src.read_json as read_json
import src.write_json as write_json

import src.tui.read_keymap as read_keymap

from colorama import Fore, Back, Style, init

def run():
    """
    edits a keymap
    :return: None
    """
    init(autoreset=True)
    while True:
        keymap_path = input("Type in the name of your layout: ")
        true_path = f"{os.path.abspath(os.getcwd())}\data\{keymap_path}.json"
        relative_path = f"data\{keymap_path}.json"

        if os.path.exists(true_path):
            break

        else:
            print(f"{Fore.RED} Keymap does not exist!")

    keymap = read_json.read(true_path)

    while True:
        for key, path in keymap.items():
            print(f"[{key}] is mapped to '{path}'")
        edit_key = input("Enter the key you would like to edit (Leave empty if done editing): ")

        if edit_key == '':
            write_json.write(f"data\{keymap_path}.json", keymap)
            print(f"{Fore.GREEN} Done!")
            input("Press enter to continue")
            return None

        edit_value = input("Enter the path to the sound file you want the key to be remapped to: ")
        keymap[edit_key] = edit_value