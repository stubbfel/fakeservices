#!/usr/bin/env python3
__author__ = 'dev'

import fake_services.utility.network.ip_address_manager as ip

# set ips
ip.add_ip_addresses(["1.1.1.1", "2.2.2.2"], "eth0")


# unset ips
#ip.remove_ip_addresses(["1.1.1.1", "2.2.2.2"], "eth0")