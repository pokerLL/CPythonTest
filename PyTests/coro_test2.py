import asyncio

async def say_after(what, delay):
    """
5 -- 5
1 -- 1
3 -- 3
9 -- 9
    """
    print(f"{what} -- {delay}")

async def main():
    # asyncio.create_task(say_after(1,1))
    # asyncio.create_task(say_after(3,3))
    # asyncio.create_task(say_after(9,9))
    g = asyncio.gather(say_after(1,1),say_after(3,3),say_after(9,9))
    await say_after("5",5)
    await g

asyncio.run(main())