import time
import asyncio

async def counter():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    tasks = [counter(), counter()]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())