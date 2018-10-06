import numpy as np
#Copyright 2018 SichunHao sichunh@bu.edu
Table = "{:<6} {:<22} {:<22} {:<22}"
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
for i in range(1,9):
	a = 2**(i*8)-1
	b = -2**(i*8-1)
	c = 2**(i*8-1)-1
	print(Table.format(i,a,b,c))
