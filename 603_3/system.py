import numpy as np
# Copyright 2018 SichunHao sichunh@bu.edu
line1 = input()
line2 = input()
a = [float(n) for n in line1.split()]
b = [float(n) for n in line2.split()]

d = [0]*(len(a)+len(b)-1)

if len(b) >= len(a): 
	n = len(b)
	m = len(a)
	for i in range(m):
		k=i
		for j in range(n):
			d[j+i] += a[i]*b[j]
else: 
	n=len(a)
	m=len(b)
	for i in range(m):
		k=i;
		for j in range(n):
			d[j+i] += a[j]*b[i]
for i in range(len(d)):
	print(d[i],end=" ")