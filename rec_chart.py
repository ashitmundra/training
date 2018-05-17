#!/usr/bin/python
import socket
import time
import matplotlib.pyplot as plt
i=0
k=0
r=[]
q=[]
rec_ip="127.0.0.1"
myport=8888
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((rec_ip, myport))
tout= int(time.time())+60
tout2=int(time.time())+30
while int(time.time())<tout :
 while int(time.time())<tout2:
  x= (s.recvfrom(1000))
  y=x[0].split()
  if x[0]=="q":
   break
  else:
   
   print ("data from client:     " +x[0])
   for j in y:
    if j=="hi":
     i=i+1  
    elif j=="hlo":
     k=k+1
 r.append(i)
 q.append(k)
 i=0
 k=0
 tout2=tout2+30
plt.plot(r,q)
plt.grid()
plt.show()


