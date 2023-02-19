import select

from collections import deque
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

def create_listen_socket(bind_addr='0.0.0.0', bind_port=55555, backlogs=102400):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((bind_addr, bind_port))
    sock.listen(backlogs)
    return sock

class Future:

    def __init__(self, loop):
        self.loop = loop
        self.done = False
        self.result = None
        self.co = None

    def set_coroutine(self, co):
        self.co = co

    def set_result(self, result):
        self.done = True
        self.result = result

        if self.co:
            self.loop.add_coroutine(self.co)

    def __await__(self):
        if not self.done:
            yield self
        return self.result

class AsyncSocket:

    def __init__(self, sock, loop):
        sock.setblocking(False)

        self.sock = sock
        self.loop = loop

    def fileno(self):
        return self.sock.fileno()

    def create_future_for_events(self, events):
        future = self.loop.create_future()

        def handler(fileno, active_events):
            self.loop.unregister_from_polling(self.fileno())
            future.set_result(active_events)

        self.loop.register_for_polling(self.fileno(), events, handler)

        return future

    async def accept(self):
        while True:
            try:
                sock, addr = self.sock.accept()
                return AsyncSocket(sock=sock, loop=self.loop), addr
            except BlockingIOError:
                future = self.create_future_for_events(select.EPOLLIN)
                await future

    async def recv(self, bufsize):
        while True:
            try:
                return self.sock.recv(bufsize)
            except BlockingIOError:
                future = self.create_future_for_events(select.EPOLLIN)
                await future

    async def send(self, data):
        while True:
            try:
                return self.sock.send(data)
            except BlockingIOError:
                future = self.create_future_for_events(select.EPOLLOUT)
                await future

class EventLoop:

    def __init__(self):
        self.epoll = select.epoll()

        self.runnables = deque()
        self.handlers = {}

    def create_future(self):
        return Future(loop=self)

    def create_listen_socket(self, bind_addr, bind_port, backlogs=102400):
        sock = create_listen_socket(bind_addr, bind_port, backlogs)
        return AsyncSocket(sock=sock, loop=self)

    def register_for_polling(self, fileno, events, handler):
        print('register fileno={} for events {}'.format(fileno, events))
        self.handlers[fileno] = handler
        self.epoll.register(fileno, events)

    def unregister_from_polling(self, fileno):
        print('unregister fileno={}'.format(fileno))
        self.epoll.unregister(fileno)
        self.handlers.pop(fileno)

    def add_coroutine(self, co):
        self.runnables.append(co)

    def run_coroutine(self, co):
        try:
            future = co.send(None)
            future.set_coroutine(co)
        except StopIteration as e:
            print('coroutine {} stopped'.format(co.__name__))

    def schedule_runnable_coroutines(self):
        while self.runnables:
            self.run_coroutine(co=self.runnables.popleft())

    def run_forever(self):
        while True:
            self.schedule_runnable_coroutines()

            events = self.epoll.poll(1)
            for fileno, event in events:
                handler = self.handlers.get(fileno)
                if handler:
                    handler(fileno, events)

class TcpServer:

    def __init__(self, loop, bind_addr='0.0.0.0', bind_port=55555):
        self.loop = loop
        self.listen_sock = self.loop.create_listen_socket(bind_addr=bind_addr, bind_port=bind_port)
        self.loop.add_coroutine(self.serve_forever())

    async def serve_client(self, sock):
        while True:
            data = await sock.recv(1024)
            if not data:
                print('client disconnected')
                break

            await sock.send(data.upper())

    async def serve_forever(self):
        while True:
            sock, (addr, port) = await self.listen_sock.accept()
            print('client connected addr={} port={}'.format(addr, port))

            self.loop.add_coroutine(self.serve_client(sock))

def main():
    loop = EventLoop()
    server = TcpServer(loop=loop)
    loop.run_forever()

if __name__ == '__main__':
    main()
