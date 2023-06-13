import asyncio
import time

import src.hotkey_handler as hotkey_handler

#tui imports
import src.tui.main_tui as main_tui
import src.tui.read_keymap as read_keymap
import src.tui.load_keymap as load_keymap
import src.tui.list_keymaps as list_keymaps

class main():
    def __init__(self):
        pass

    async def run(self, keymap_path):
        listener1 = asyncio.create_task(hotkey_handler.listener(1, keymap_path))
        # listener2 = asyncio.create_task(hotkey_handler.listener(2))
        # listener3 = asyncio.create_task(hotkey_handler.listener(3))
        # listener4 = asyncio.create_task(hotkey_handler.listener(4))
        # listener5 = asyncio.create_task(hotkey_handler.listener(5))

        # tasks = [listener1, listener2, listener3, listener4, listener5]
        tasks = [listener1]

        await asyncio.gather(*tasks)

if __name__ == '__main__':
    main = main()
    DELAY = 0.1
    default_keymap = "data/keymap.json"

    while True:
        val = main_tui.run()

        match val:
            case 1:
                pass
            case 2:
                read_keymap.run(default_keymap)
            case 3:
                default_keymap = load_keymap.run()
            case 4:
                print("Soundpad started! Press and hold Control+C to stop the soundpad")

                while True:
                    asyncio.run(main.run(default_keymap))
                    time.sleep(DELAY)
            case 5:
                list_keymaps.run()
