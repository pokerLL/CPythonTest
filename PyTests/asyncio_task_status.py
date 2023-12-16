import asyncio
import threading
import time

async def hello():
    print("Running in the loop...")
    flag = 0
    while flag < 1000:
        with open("F:\\test.txt", "a") as f:
            f.write("------")
        flag += 1
    print("Stop the loop")

if __name__ == '__main__':
    coroutine = hello()
    loop = asyncio.get_event_loop()
    task = loop.create_task(coroutine)

    # Pending：未执行状态
    print(task)
    try:
        t1 = threading.Thread(target=loop.run_until_complete, args=(task,))
        # t1.daemon = True
        t1.start()

        # Running：运行中状态
        time.sleep(1)
        print(task)
        t1.join()
    except KeyboardInterrupt as e:
        # 取消任务
        task.cancel()
        # Cacelled：取消任务
        print(task)
    finally:
        print(task)

"""
<Task pending name='Task-1' coro=<hello() running at /workspace/program/CPythonTest/PyTests/asyncio_task_status.py:5>>
Running in the loop...
Stop the loop
<Task finished name='Task-1' coro=<hello() done, defined at /workspace/program/CPythonTest/PyTests/asyncio_task_status.py:5> result=None>
<Task finished name='Task-1' coro=<hello() done, defined at /workspace/program/CPythonTest/PyTests/asyncio_task_status.py:5> result=None>
"""