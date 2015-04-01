__author__ = 'dev'

from socketserver import ThreadingUDPServer
from fakedns import DNSHandler
from fake_services.service.fake_server_manager import FakeServerManager

DEFAULT_DNS_PORT = 53


class FakeDnsServerManager(FakeServerManager):
    def __init__(self, server_port=DEFAULT_DNS_PORT):
        super().__init__(ThreadingUDPServer, DNSHandler, server_port, **{"bind_and_activate": True})