__author__ = 'dev'
import threading


class FakeServerManager:

    def __init__(self, server_class, request_handler_class, server_port, **kwargs):
        self.server = server_class(('', server_port), request_handler_class, kwargs)

    def start_server(self):
        threading.Thread(target=self.server.serve_forever).start()

    def stop_server(self):
        self.server.shutdown()