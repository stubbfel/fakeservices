from http.server import HTTPServer

__author__ = 'dev'


class FakeWebServer(HTTPServer):

    def __init__(self, server_address, request_handler_class, requests_config):
        super().__init__(server_address, request_handler_class)
        self.requests_config = requests_config