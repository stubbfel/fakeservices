from fake_services.service.networkservice.fake_dns_server_manager import FakeDnsServerManager

__author__ = 'dev'

import unittest


class TestFakeDns(unittest.TestCase):

    def test_dns_server_start_stop(self):
        manager = FakeDnsServerManager(8080)
        manager.start_server()
        manager.stop_server()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
