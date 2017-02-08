#!/usr/bin/env python

import sys
import socket
from time import sleep
from threading import Thread
from SocketServer import ThreadingMixIn
import struct

TCP_IP = raw_input("Your IP ? : ")
TCP_PORT_SEND = 60005
BUFFER_SIZE = 1024

def add_nbr(nbr):
    if nbr == 32:
        nbr = 44
    elif nbr == 57:
        nbr = 65
    elif nbr == 90:
        nbr = 97
    elif nbr == 0:
        nbr = 32
    else:
        nbr = nbr + 1
    return nbr

def dec2bin(d):
    b = ""
    nb = 8
    if d == 0:
        return "0".zfill(nb)
    if d < 0:
        d += 1 << nb
    while d != 0:
        d, r = divmod(d, 2)
        b = "01"[r] + b
    return b.zfill(nb)

class ClientThread_send(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print " New thread started for "+ip+":"+str(port)
        
    def run(self):
        global d

        self.sock.send(msg)
        sleep(2)
        val = dec2bin(d)
        self.sock.send(val)
        print ("from " + str(d)),
        d = add_nbr(d)
        d = add_nbr(d)
        d = add_nbr(d)
        print "to " + str(d)
        d = add_nbr(d)
        print('Successefully sent the data')
        self.sock.close()
        
def server_lauch(msg_tmp):
    global d
    global msg
    global result

    d = 0
    msg = msg_tmp
    result = []

    IP = raw_input("IP server ? : ")
    print 'TCP_IP =',IP
    print 'TCP_PORT_SEND =',TCP_PORT_SEND
    print 'TCP_PORT_RECV =',TCP_PORT_RECEIVE
                    
    tcpsock_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock_send.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock_send.bind((IP, TCP_PORT_SEND))
    threads_send = []

    while d < 126:
        sleep(3)
        tcpsock_send.listen(5)
        (conn, (ip,port)) = tcpsock_send.accept()
        print 'Got connection to send from ', (ip,port)
        newthread_send = ClientThread_send(ip,port,conn)
        newthread_send.start()
        threads_send.append(newthread_send)

    for t in threads_send:
        t.join()
