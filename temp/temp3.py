import asyncio

async def k(e):
    return e



async def main():
    task = k(1)
    task2 = k(2)

    asyncio.gather(task, task2)

    print(task, task2)

asyncio.run(main())