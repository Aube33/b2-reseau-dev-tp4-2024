import asyncio
import aioconsole
import sys

async def receiveResponses(reader):
    while True:
        data = await reader.read(1024)
        if data == b'':
            print("Annonce : Le serveur est hors ligne")
            return
        
        print(">>> ",data.decode())

async def sendData(writer):
    while True:
        message = await aioconsole.ainput()
        msg = message.encode()
        writer.write(msg)
        await writer.drain()
        
async def main():
    pseudo = input("Pseudo: ")

    reader, writer = await asyncio.open_connection(host="127.0.0.1", port=8888)

    writer.write(f"Hello|{pseudo}".encode())

    tasks = [receiveResponses(reader), sendData(writer)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())