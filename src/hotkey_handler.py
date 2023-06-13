import keyboard

from src import read_json

from src import os_pipe

# def listener(key):
#     print("pass")
#     pass

async def listener(thread):
    """
    :param thread: variable used for asyncronous programming and debugging
    :return: None
    """
    # Reads keymap data from keymap json file
    keymap = read_json.read('data/keymap.json')
    #print(f'Listener running on thread {thread}') (THIS WAS A STUB)

    key_list = list()
    path_list = list()

    for key, path in keymap.items():
        key_list.append(key)
        path_list.append(path)

        if keyboard.is_pressed(key):
            # needs to pipe arguments into os_pipe which runs a separate subprocess because playing audio pauses python
            # until audio is done playing
            os_pipe.play(path)

# old depreciated function to handle keymaps
"""
def load():
    keymap = read_json.read('data/keymap.json')


    print("loading")
    for key, path in keymap.items():a
        print(f"Syncing {key} to {path}")
        keyboard.add_hotkey(key, lambda: playsound.play(path))
        print("doneq")

    print("complete")
"""