__author__ = 'dev'

import threading
from fake_services.service.webservice.fake_http_request_handler import FakeHTTPRequestHandler
from fake_services.service.webservice.fake_web_server import FakeWebServer


class FakeWebServerManager:

    def __init__(self, server_port, requests_config=None):
        self.server = FakeWebServer(('', server_port), FakeHTTPRequestHandler, requests_config)

    def start_server(self):
        threading.Thread(target=self.server.serve_forever).start()

    def stop_server(self):
        self.server.shutdown()