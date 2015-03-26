__author__ = 'dev'

import os
import re
import unittest

import fake_services.utility.network.ip_address_manager as ip


FIRST_IP_ADDRESS = "1.1.1.1"
SECOND_IP_ADDRESS = "1.1.1.2"
NETWORK_DEVICE_NAME = "enp20s0"


class TestIpManager(unittest.TestCase):

    def tearDown(self):
        ip.remove_ip_address(FIRST_IP_ADDRESS, NETWORK_DEVICE_NAME)
        ip.remove_ip_address(SECOND_IP_ADDRESS, NETWORK_DEVICE_NAME)

    def test_add_address(self):
        self.assertFalse(self.ping_able(FIRST_IP_ADDRESS))
        ip.add_ip_address(FIRST_IP_ADDRESS, NETWORK_DEVICE_NAME)
        self.assertTrue(self.ping_able(FIRST_IP_ADDRESS))

    def test_add_addresses(self):
        self.assertFalse(self.ping_able(FIRST_IP_ADDRESS))
        self.assertFalse(self.ping_able(SECOND_IP_ADDRESS))
        ip.add_ip_addresses([FIRST_IP_ADDRESS,SECOND_IP_ADDRESS], NETWORK_DEVICE_NAME)
        self.assertTrue(self.ping_able(FIRST_IP_ADDRESS))
        self.assertTrue(self.ping_able(SECOND_IP_ADDRESS))

    def test_rm_addresses(self):
        self.assertFalse(self.ping_able(FIRST_IP_ADDRESS))
        self.assertFalse(self.ping_able(SECOND_IP_ADDRESS))
        ip.add_ip_addresses([FIRST_IP_ADDRESS,SECOND_IP_ADDRESS], NETWORK_DEVICE_NAME)
        self.assertTrue(self.ping_able(FIRST_IP_ADDRESS))
        self.assertTrue(self.ping_able(SECOND_IP_ADDRESS))
        ip.remove_ip_addresses([FIRST_IP_ADDRESS,SECOND_IP_ADDRESS], NETWORK_DEVICE_NAME)
        self.assertFalse(self.ping_able(FIRST_IP_ADDRESS))
        self.assertFalse(self.ping_able(SECOND_IP_ADDRESS))

    def test_rm_address(self):
        self.assertFalse(self.ping_able(FIRST_IP_ADDRESS))
        ip.add_ip_address(FIRST_IP_ADDRESS, NETWORK_DEVICE_NAME)
        self.assertTrue(self.ping_able(FIRST_IP_ADDRESS))
        ip.remove_ip_address(FIRST_IP_ADDRESS, NETWORK_DEVICE_NAME)
        self.assertFalse(self.ping_able(FIRST_IP_ADDRESS))

    def test_massive_adds(self):
        ip_prefix = "10.0.0."
        ip_list = []

        for i in range(0, 255):
            ip_list.append(ip_prefix + (str(i)))

        try:
            ip.add_ip_addresses(ip_list, NETWORK_DEVICE_NAME)
            for ip_address in ip_list:
                self.assertTrue(self.ping_able(ip_address))
        finally:
            ip.remove_ip_addresses(ip_list, NETWORK_DEVICE_NAME)

    def ping_able(self, ip_address):
        cmd = "ping -c1 " + ip_address
        r = "".join(str(os.popen(cmd).readlines()))
        if re.search("64 bytes from", r):
            return True
        else:
            return False

if __name__ == '__main__':
    unittest.main()
