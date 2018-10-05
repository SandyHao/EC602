#Copyright 2018 SichunHao sichunh@bu.edu
import sys

for i in range(len(sys.argv)):  
	if i<=4 and i>=1:
		sys.stdout.write(sys.argv[i]+'\n')
	elif i>=5:
		sys.stderr.write(sys.argv[i]+'\n')
