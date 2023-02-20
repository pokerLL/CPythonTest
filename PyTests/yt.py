def yfun():
    print(1)
    yield 1
    print(2)
    yield 2

async def fun():
    res1 = yield yfun()
    print(res1)


if __name__ ==  "__main__":
    fun().send(None)