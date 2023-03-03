import asyncio

async def say_after(what, delay):
    await asyncio.sleep(delay)
    """
1 -- 1
3 -- 3
5 -- 5
9 -- 9
    """
    # asyncio.sleep(delay)
    """
d:/Program/Workspace/CPythonTest/PyTests/coro.py:11: RuntimeWarning: coroutine 'sleep' was never awaited
  asyncio.sleep(delay)
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
5 -- 5
1 -- 1
3 -- 3
9 -- 9
    """
    print(f"{what} -- {delay}")

async def main():
    g = asyncio.gather(say_after(1,1),say_after(3,3),say_after(9,9))
    await say_after("5",5)
    await g

asyncio.run(main())