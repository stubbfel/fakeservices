#!/bin/bash
sudo ip addr add 172.20.0.1/16 dev br0
sudo ip link set br0 up
sudo dnsmasq --interface=br0 --bind-interfaces --dhcp-range=172.20.0.2,172.20.255.254
sudo modprobe virtio
qemu-system-i386 -m 512 -enable-kvm -net nic -net bridge,br=br0 ~/Downloads/FakeServices32B.i686-0.1.2.qcow2
