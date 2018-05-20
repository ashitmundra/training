#!/usr/bin/python
import time
import webbrowser
import socket
import requests
import whois
from bs4 import BeautifulSoup
import os
import commands
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
	a=raw_input("Enter any word    ")
	url = ("http://www.google.com/search?q=%s"%a)
	response = requests.get(url)
	# parse html
	page = str(BeautifulSoup(response.content))


 	def getURL(page):
    
    		start_link = page.find("a href")
    		if start_link == -1:
        		return None, 0
    		start_quote = page.find('"', start_link)
    		end_quote = page.find('"', start_quote + 1)
    		url = page[start_quote + 1: end_quote]
    		return url, end_quote

	while True:
    		url, n = getURL(page)
    		page = page[n:]
    		if url:
        		print url
    		else:
        		break
	
elif choice=="4" :
	print time.ctime()
elif choice=="5" :
	webbrowser.open_new_tab('http://')
elif choice=="6" :
	print commands.getoutput("sudo arp-scan -l --interface=wlo1")

elif choice=="7" :
	a=raw_input("Enter any statement    ")
	w=whois.whois(a)
	print w.domain_name
	print w.emails
else :
	print "Wrong Input"







