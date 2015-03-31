from fake_services.service.fake_server_manager import FakeServerManager

__author__ = 'dev'

from fake_services.service.webservice.fake_http_request_handler import FakeHTTPRequestHandler
from fake_services.service.webservice.fake_web_server import FakeWebServer


class FakeWebServerManager(FakeServerManager):

    def __init__(self, server_port, requests_config=None):
        super().__init__(FakeWebServer, FakeHTTPRequestHandler, server_port, **requests_config)