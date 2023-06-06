import keyboard

from src import playsound
from src import read_json

def load():
    keymap = read_json.read('data/keymap.json')

    print("loading")
    for key, path in keymap.items():
        print(f"Syncing {key} to {path}")
        keyboard.add_hotkey(key, lambda: playsound.play(path))

    print("complete")
