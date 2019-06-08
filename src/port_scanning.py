from src.sockets import RawSocket
from src.host import Host
from src.tcpFlags import TCPFlags
from src.constants import *

sourceMAC = [0x08, 0x00, 0x27, 0x10, 0x52, 0x48]
sourceIP = '2804:14d:4c84:9530:a00:27ff:fe10:5248'#'fe80::a00:27ff:fe10:5248'
sourcePort = 3000

destMAC = [0x8c, 0x85, 0x90, 0x43, 0xba, 0x9f] # 8c:85:90:43:ba:9f
destIP = '2804:14d:4c84:9530:149f:ba6e:2008:5864'

def tcp_connect(port):

    socket = RawSocket()
    print('Ataque TCP Connect na porta ', port)
    source = Host(sourceMAC, sourceIP, sourcePort)
    dest = Host(destMAC, destIP, port)
    syn = TCPFlags(0, 1, 0, 0, 0, 0)

    socket.send(source, dest, syn)

    received_flags = socket.receive(dest)
    if received_flags == SYNACK:
        ack = TCPFlags(0, 0, 0, 0, 1, 0)
        socket.send(source, dest, ack)
        print('PORTA ABERTA')
    else:
        print('PORTA FECHADA')

def tcp_half_opening(port):

    socket = RawSocket()
    print('Ataque TCP Half-Opening na porta ', port)
    source = Host(sourceMAC, sourceIP, sourcePort)
    dest = Host(destMAC, destIP, port)
    syn = TCPFlags(0, 1, 0, 0, 0, 0)

    socket.send(source, dest, syn)

    received_flags = socket.receive(dest)
    if received_flags == SYNACK:
        rst = TCPFlags(0, 0, 1, 0, 0, 0)
        socket.send(source, dest, rst)
        print('PORTA ABERTA')
    else:
        print('PORTA FECHADA')

def tcp_stealth_scan(port):

    socket = RawSocket()
    print('Ataque Stealth Scan na porta ', port)
    source = Host(sourceMAC, sourceIP, sourcePort)
    dest = Host(destMAC, destIP, port)
    fin = TCPFlags(1, 0, 0, 0, 0, 0)

    socket.send(source, dest, fin)

    received_flags = socket.receive(dest)
    if received_flags == RSTACK:
        print('PORTA FECHADA')
    else:
        print('PORTA ABERTA')

def tcp_syn_ack(port):

    socket = RawSocket()
    print('Ataque SYN/ACK na porta ', port)
    source = Host(sourceMAC, sourceIP, sourcePort)
    dest = Host(destMAC, destIP, port)
    syn_ack = TCPFlags(0, 1, 0, 0, 1, 0)

    socket.send(source, dest, syn_ack)

    received_flags = socket.receive(dest)
    if received_flags == RST:
        print('PORTA ABERTA')
    else:
        print('PORTA FECHADA')

        
