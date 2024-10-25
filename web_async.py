import aiohttp
import aiofiles
import sys
import asyncio

DL_FILE = "/tmp/web_page"

async def write_content(content:str, file:str):
    async with aiofiles.open(file, mode="w", encoding="utf-8") as out:
        await out.write(content.decode())
        await out.flush() 

async def get_content(url:str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp = await resp.read()
            return resp

async def main():
    argv = sys.argv[1:]
    if len(argv)==0:
        print("Usage: python web_async.py <URL>")
    else:
        url_request = argv[0]
        html_content = await get_content(url_request)
        await write_content(html_content, DL_FILE)

if __name__ == "__main__":
    asyncio.run(main())