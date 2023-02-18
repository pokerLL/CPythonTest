import asyncio
import time

async def block_func(block_duration: float = 5) -> None:
    print(locals())

    # Blocking the event loop for 5 seconds
    time.sleep(block_duration)
    print(locals())

async def sleep_func(sleep_duration: float = 1) -> None:
    print(locals())

    start_time = time.time()
    await asyncio.sleep(delay=sleep_duration)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Expected asynchronous sleep duration: {:.2f}s.".format(sleep_duration))
    print("Actual asynchronous sleep duration: {:.2f}s.".format(elapsed_time))
    print(locals())

block_duration = 5
sleep_duration = 1

loop = asyncio.get_event_loop()

print("="*50)
print("Scheduled blocking first...")
print("-"*50)
loop.run_until_complete(
    asyncio.gather(
        block_func(block_duration),
        sleep_func(sleep_duration),
    )
)
print("="*50)
print("Scheduled sleeping first...")
print("-"*50)
loop.run_until_complete(
    asyncio.gather(
        sleep_func(sleep_duration),
        block_func(block_duration),
    )
)
print("="*50)
