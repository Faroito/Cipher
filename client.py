#!/usr/bin/env python

from time import sleep
import socket
import sys
from threading import Thread
from SocketServer import ThreadingMixIn
from fractions import Fraction
from fractions import gcd

try:
    IP = sys.argv[1]
except IndexError:
    IP = raw_input("IP server ? : ")

TCP_PORT_SEND = 60005
BUFFER_SIZE = 1024

def with_zero(string, n):
    while len(string) % n != 0:
        string = string + str('\0')
    return string

def size(string, n):
    size = len(string) / n
    return size

def matrix_create(l_max, c_max, matrix, string, m_type):
    i = 0
    c = 0
    l = 0
    while l < l_max:
        while c < c_max:
            if m_type == 0:
                matrix[l][c] = ord(string[i])
            else:
                matrix[l][c] = string[i]
            c = c + 1
            i = i + 1
        c = 0
        l = l + 1
    return matrix

def calcul_det(matrix):
    result = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    return result

def matrix_calcul_bis(l, c, matrix_msg, matrix_key, square_size):
    result = 0
    i = 0
    while i < square_size:
        result = result + (matrix_msg[i][c] * matrix_key[l][i])
        i = i + 1
    if (0 <= int(result) and int(result) <= 127):
        if gcd(result, 1) == 1:
            return (unichr(int(result)), 0)
        else:
            return (unichr(0), 1)
    else:
        return (unichr(0), 1)
                                                

def print_string(string):
    i = 0
    print ("The message could be : \""),
    while i < len(string):
        sys.stdout.write(string[i])
        i = i + 1
    print "\""

def decrypting(l_max, c_max, matrix_msg, matrix_key):
    c = 0
    l = 0
    end = 0
    string = []
    while l < l_max and end == 0:
        while c < c_max and end == 0:
            tmp, tmp2 = matrix_calcul_bis(l, c, matrix_msg, matrix_key, c_max)
            end = end + tmp2
            string.append(tmp)
            c = c + 1
        c = 0
        l = l + 1
    if end == 0:
        print_string(string)

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
            
def breaking_2_key(matrix_msg, msg, d, d_max):
    a = 32
    b = 32
    c = 32
    while d <= d_max:
        matrix_tmp = [[0] * (2) for _ in range(2)]
        matrix_tmp[0][0] = a
        matrix_tmp[0][1] = b
        matrix_tmp[1][0] = c
        matrix_tmp[1][1] = d
        det = calcul_det(matrix_tmp)
        if det != 0:
            det = Fraction(1, det)
            matrix_key = [[0] * (2) for _ in range(2)]
            matrix_key[0][0] = det * matrix_tmp[1][1]
            matrix_key[1][1] = det * matrix_tmp[0][0]
            matrix_key[0][1] = det * -1 * matrix_tmp[0][1]
            matrix_key[1][0] = det * -1 * matrix_tmp[1][0]
            decrypting(size(msg, 2), 2, matrix_key, matrix_msg)
        a = add_nbr(a)
        if a == 123:
            a = 32
            b = add_nbr(b)
            if b == 123:
                b = 32
                c = add_nbr(c)
                if c == 123:
                    c = 32
                    d = add_nbr(d)
                    
print "/!\\ Starting research /!\\"

while True :
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, TCP_PORT_SEND))
        msg_tmp = s.recv(BUFFER_SIZE)
        sleep(0.5)
        buf = s.recv(8)
        d = int(buf, 2)
        d_max = add_nbr(d)
        d_max = add_nbr(d_max)
        d_max = add_nbr(d_max)
        s.close()

        msg = [int(x) for x in msg_tmp.split()]
        msg = with_zero(msg, 2)
        matrix_msg = [[0] * 2 for _ in range(size(msg, 2))]
        matrix_msg = matrix_create(size(msg, 2), 2, matrix_msg, msg, 1)
        breaking_2_key(matrix_msg, msg, d, d_max)
    except socket.error :
        print "/!\\ No server connection /!\\ (or all key done)"
        break
