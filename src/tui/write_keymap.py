import os

import src.write_json as write_json


def run():
    keymap = {}

    while True:
        keymap_path = input("Type in the name of your layout: ")
        true_path = f"{os.path.abspath(os.getcwd())}\data\{keymap_path}.json"

        if os.path.exists(true_path):
            print(f"Layout already exists!")

        else:
            break

    while True:
        key = input("Enter a key that will be bound to a sound (Press ENTER when you are done)")

        if key == '':
            write_json.write(f"data\{keymap_path}.json3", keymap)
            print("Done!")
            return

        sound_path = input("Enter the path to where the sound file will be located (Has to be a .wav file and is reccomended"
                           "to be placed in the /sounds/ folder")

        keymap[key] = sound_path
        print(key)

