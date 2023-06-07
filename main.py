import asyncio
import time

import src.hotkey_handler as hotkey_handler

class main():
    def __init__(self):
        pass

    async def run(self):
        hotkey_handler.load()

        listener1 = asyncio.create_task(hotkey_handler.listener(1))

        tasks = [listener1]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    main = main()
    DELAY = 1

    while True:
        asyncio.run(main.run())


