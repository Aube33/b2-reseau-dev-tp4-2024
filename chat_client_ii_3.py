import asyncio
import aioconsole

async def receiveResponses(reader):
    while True:
        data = await reader.read(1024)
        print("\n",data.decode(), "\n")

async def sendData(writer):
    while True:
        message = await aioconsole.ainput()
        msg = message.encode()
        writer.write(msg)
        await writer.drain()

async def main():
    reader, writer = await asyncio.open_connection(host="127.0.0.1", port=8888)

    tasks = [receiveResponses(reader), sendData(writer)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())