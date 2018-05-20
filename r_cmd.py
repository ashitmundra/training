#!/usr/bin/python
import socket
import time
import matplotlib.pyplot as plt
rec_ip="127.0.0.1"
myport=8888
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((rec_ip, myport))
  while 3>2:
   x= (s.recvfrom(1000))
   if x=="q":
    break
   else:
   
    print ("data from client:     " +x)


