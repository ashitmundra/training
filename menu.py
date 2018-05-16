#!/usr/bin/python
import time
import webbrowser
import socket
print "Option 1"
print "Option 2"
print "Option 3"
print "Option 4"
print "Option 5"
print "Option 6"
print "Option 7"
choice=raw_input("Enter any choice")
if choice=='1' :
	a=raw_input("Enter any statement    ")
	b=a.split()
	for i in b :
		webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % i)
elif choice=="2" :
	c=raw_input("Enter any statement    ")
	d=c.split()
	for j in d:
		webbrowser.open_new_tab('https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj4xsXjn4fbAhWFE5QKHeDpDUgQ_AUIDCgD&biw=1391&bih=662' % j)
elif choice=="3" :
	raw_input("Enter any statement    ")
elif choice=="4" :
	print time.ctime()
elif choice=="5" :
	webbrowser.open_new_tab('http://')
elif choice=="6" :
	raw_input("Enter any statement    ")
elif choice=="7" :
	raw_input("Enter any statement    ")
else :
	print "Wrong Input"







