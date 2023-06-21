import asyncio
import time

import src.hotkey_handler as hotkey_handler

#tui imports
import src.tui.main_tui as main_tui
import src.tui.read_keymap as read_keymap
import src.tui.load_keymap as load_keymap
import src.tui.list_keymaps as list_keymaps
import src.tui.write_keymap as write_keymap
import src.tui.edit_keymap as edit_keymap

from colorama import Fore


class main():
    def __init__(self):
        pass

    async def run(self, keymap_path):
        listener1 = asyncio.create_task(hotkey_handler.listener(1, keymap_path))
        # listener2 = asyncio.create_task(hotkey_handler.listener(2))
        # listener3 = asyncio.create_task(hotkey_handler.listener(3))
        # listener4 = asyncio.create_task(hotkey_handler.listener(4))
        # listener5 = asyncio.create_task(hotkey_handler.listener(5))
        # DRIVER_LISTENER = asyncio.create_task(hotkey_handler.listener(6, "data/keymap.json")

        # tasks = [listener1, listener2, listener3, listener4, listener5]
        tasks = [listener1]

        await asyncio.gather(*tasks)
        # await asyncio.gather(listener1, listener2)

if __name__ == '__main__':
    main = main()
    DELAY = 0.1
    default_keymap = "data/keymap.json"

    while True:
        val = main_tui.run()

        match val:
            case 1:
                write_keymap.run()
            case 2:
                read_keymap.run(default_keymap)
            case 3:
                default_keymap = load_keymap.run()
            case 4:
                print(f"{Fore.GREEN} Soundpad started! Press and hold Control+C to stop the soundpad")

                while True:
                    asyncio.run(main.run(default_keymap))
                    time.sleep(DELAY)
            case 5:
                list_keymaps.run()
            case 6:
                edit_keymap.run()

