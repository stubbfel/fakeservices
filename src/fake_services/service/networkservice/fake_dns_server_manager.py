from fake_services.service.fake_server_manager import FakeServerManager

__author__ = 'dev'

import threading
from socketserver import ThreadingUDPServer
from fakedns import DNSHandler


class FakeDnsServerManager(FakeServerManager):
    def __init__(self, server_port):
        super().__init__(ThreadingUDPServer, DNSHandler, server_port, **{"bind_and_activate": True})
        #self.server = ThreadingUDPServer(('', server_port), DNSHandler)
