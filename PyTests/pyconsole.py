import code
import threading
import sys

from io import StringIO
from xmlrpc.client import ServerProxy
from xmlrpc.server import SimpleXMLRPCServer

class OutputHookContext:

    def __enter__(self):
        self.output = StringIO()

        self.sys_stdout = sys.stdout
        sys.stdout = self.output

        self.sys_stderr = sys.stderr
        sys.stderr = self.output

    def __exit__(self, *args, **kwargs):
        sys.stdout = self.sys_stdout
        sys.stderr = self.sys_stderr

    def getOutput(self):
        return self.output.getvalue()

class CodeRunner:

    def __init__(self):
        self.interpreter = code.InteractiveInterpreter()
        self.lock = threading.RLock()
        self.output_hook = OutputHookContext()

        self.run('import __main__ as main')
        self.run('import sys')

    def run(self, code, filename='<input>', symbol='single'):
        with self.lock:
            with self.output_hook:
                more = self.interpreter.runsource(code, filename, symbol)
                output = self.output_hook.getOutput()
                return more, output

class ConsoleServer:

    def __init__(self, addr='127.0.0.1', port=44444, code=''):
        self.addr = addr
        self.port = port
        self.code = code

    def serve_forever(self):
        with SimpleXMLRPCServer((self.addr, self.port), logRequests=False) as server:
            server.register_introspection_functions()
            server.register_instance(CodeRunner())
            server.serve_forever()

    def serve_in_new_thread(self, thread_name=None):
        self._thread = threading.Thread(target=self.serve_forever)
        self._thread.setName(thread_name or ConsoleServer.__name__)
        self._thread.setDaemon(True)
        self._thread.start()

class ConsoleClient(code.InteractiveConsole):

    def __init__(self, addr='127.0.0.1', port=44444):
        super().__init__()

        self.addr = addr
        self.port = port

        self.uri = 'http://{addr}:{port}/'.format(
            addr=self.addr,
            port=self.port,
        )
        self.proxy = ServerProxy(self.uri)

    def runsource(self, source, filename='<stdin>', symbol='single'):
        more, output = self.proxy.run(source, filename, symbol)
        if output:
            self.write(output)

        return more

def start_console_server(port=44444, addr='127.0.0.1', code='', thread_name=ConsoleServer.__name__, startup=True):
    server = ConsoleServer(addr=addr, port=port, code=code)
    if startup:
        server.serve_in_new_thread(thread_name=thread_name)
    return server

def run_console_client(port=44444, addr='127.0.0.1'):
    client = ConsoleClient(addr=addr, port=port)
    client.interact()

if __name__ == '__main__':
    run_console_client()