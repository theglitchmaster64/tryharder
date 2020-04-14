#!/usr/bin/env python3

import os
import sys
import socket

#packet struct : command arg

command = [b'STATS ',b'RTIME ',b'LTIME ',b'SRUN ',b'TRUN ',b'GMON ',b'GDOG ',b'LTER ',b'KSTAN ']

vulncommands = [b'KSTET ',b'GTER ']

excepts = [b'HTER ']

buff=b'A'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    conn=s.connect(('192.168.43.186',9999))
    resp=s.recv(1024)
    print(resp.decode())

    if(len(sys.argv)==1):
        for x in range(0,len(command)):
            for i in range(50,20000,50):
                print('fuzzing command:{0}, with length {1}'.format(command[x],i))
                s.send(command[x]+(buff*i))
                resp=s.recv(1024)
                print(resp.decode())

    if(len(sys.argv)==2):
        for i in range(50,350,1):
            print('fuzzing command:{0}, with length {1}'.format(command[7],i))
            s.send(command[7]+(buff*i))
            resp=s.recv(1024)
            print(resp.decode())

    else:
        print('incorrect useage')
