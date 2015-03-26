__author__ = 'dev'

import subprocess
import ipaddress

SUDO_CMD = "sudo"
IP_CMD = "ip"
ADDR_ARG = "addr"
ADD_ARG = "add"
RM_ARG = "del"
DEV_ARG = "dev"


def add_ip_address(ip_address, network_card):
    add_or_remove_address(ip_address, network_card, ADD_ARG)


def remove_ip_address(ip_address, network_card):
    add_or_remove_address(ip_address, network_card, RM_ARG)


def add_ip_addresses(ip_addresses, network_card):
    for ip_address in ip_addresses:
        add_or_remove_address(ip_address, network_card, ADD_ARG)


def remove_ip_addresses(ip_addresses, network_card):
    for ip_address in ip_addresses:
        add_or_remove_address(ip_address, network_card, RM_ARG)


def add_or_remove_address(ip_address, network_card, cmd):
    ipaddress.ip_address(ip_address)
    subprocess.call([SUDO_CMD, IP_CMD, ADDR_ARG, cmd, ip_address, DEV_ARG, network_card])
