import asyncio

import src.hotkey_handler as hotkey_handler

class main():
    def __init__(self):
        pass

    async def run(self):
        hotkey_handler.load()

if __name__ == '__main__':
    main = main()
    asyncio.run(main.run())
