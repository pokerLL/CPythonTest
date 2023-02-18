import asyncio
async def fun2():
    return 1

async def fun():
    await fun2()

asyncio.run(fun())