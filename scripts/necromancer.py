#!/usr/bin/env python3
"""
Project Verithrax Ark - Necromancer Protocol
Description: Wake-on-LAN trigger for Hybrid x86 Nodes based on Kubernetes pending pods.
Author: Verithrax Xeon
"""

import socket
import struct
import time
import os
import sys

# Configuration
TARGET_MAC = "64:6E:E0:58:27:4E"  # Replace with GP66 MAC
TARGET_IP = "192.168.68.100"      # Static IP of the Beast
BROADCAST_IP = "192.168.68.255"
PORT = 9

def create_magic_packet(macaddress):
    """Create a standard WoL Magic Packet."""
    if len(macaddress) == 12:
        pass
    elif len(macaddress) == 17:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, '')
    else:
        raise ValueError('Incorrect MAC address format')
    
    data = b'FFFFFFFFFFFF' + (macaddress.encode() * 16)
    send_data = b''
    for i in range(0, len(data), 2):
        send_data += struct.pack('B', int(data[i: i + 2], 16))
    return send_data

def summon_the_beast():
    """Sends the Magic Packet to wake the x86 node."""
    print(f"[*] Necromancer Protocol Initiated: Summoning {TARGET_MAC}...")
    packet = create_magic_packet(TARGET_MAC)
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.connect((BROADCAST_IP, PORT))
        sock.send(packet)
        
    print("[+] Magic Packet sent. Waiting for heartbeat...")

def check_pulse(retries=30):
    """Pings the target to verify it's awake."""
    for i in range(retries):
        response = os.system(f"ping -c 1 -W 1 {TARGET_IP} > /dev/null 2>&1")
        if response == 0:
            print(f"[+] The Beast is AWAKE at {TARGET_IP}!")
            return True
        time.sleep(2)
        print(f"[-] Pulse check {i+1}/{retries}...")
    return False

if __name__ == "__main__":
    summon_the_beast()
    if check_pulse():
        sys.exit(0)
    else:
        print("[!] Summoning failed. Check power delivery.")
        sys.exit(1)