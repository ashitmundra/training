#!/usr/bin/python
import socket
i=1
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while i:
 a=raw_input()
 if a=="q":
  s.sendto(a, ("127.0.0.1", 8888))
  break
 else:
  s.sendto(a, ("127.0.0.1", 8888))


