import asyncio

CLIENTS = {}

async def handle_client_msg(reader, writer):
    global CLIENTS
    while True:
        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')

        CLIENTS[addr] = {}
        CLIENTS[addr]["r"] = reader
        CLIENTS[addr]["w"] = writer

        if data == b'':
            break

        message = data.decode()
        print(f"Message received from {addr[0]}:{addr[1]} : {message!r}")

        for client in CLIENTS.keys():
            if client != addr:
                CLIENTS[client]["w"].write(f"{addr[0]}:{addr[1]} a dit : {message}".encode())
        await writer.drain()

async def main():
    server = await asyncio.start_server(handle_client_msg, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
