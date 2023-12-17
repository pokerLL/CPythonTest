import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        # 发起网络请求并获取请求结果的 Future 对象
        future = asyncio.ensure_future(fetch_url(session, 'https://www.example.com'))

        # 等待请求结果返回
        await future

        # 在请求结果返回后，将结果设置到 Future 对象中
        # future.set_result('Request completed successfully')

        # 获取请求结果并打印
        result = future.result()
        print(result)

asyncio.run(main())