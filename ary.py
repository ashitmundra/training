#!/usr/bin/python3
n=int(input("no. of inputs"))
j=0
while(j<n) :
	input("enter number")
	j=j+1
def a(n):
	i=2
	flag=0
	while(i<n) :
		if (n%i==0) :
			print("matrix possible :")
			print ((i, int(n/i)))
			flag=1
		i=i+1
	if (flag==0):
		print("no matrix can be found enter one more input")
		input("pne more number")
		print("now final matrix possible:")
		a(n+1)
	return;
a(n)
	

	
