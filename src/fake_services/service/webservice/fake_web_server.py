from http.server import HTTPServer

__author__ = 'dev'


class FakeWebServer(HTTPServer):

    def __init__(self, server_address, request_handler_class, request_handle_script_path, requests_config):
        super().__init__(server_address, request_handler_class)
        self.request_handle_script_path = request_handle_script_path
        self.requests_config = requests_config