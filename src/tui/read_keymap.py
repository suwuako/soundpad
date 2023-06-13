import os

import src.read_json as read_json


def run(keymap_path):
    localpath = f"{os.path.abspath(os.getcwd())}\{keymap_path}"

    keymap = read_json.read(localpath)

    for key, path in keymap.items():
        print(f"[{key}] is mapped to '{path}'")