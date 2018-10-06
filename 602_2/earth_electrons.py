import numpy
#Copyright 2018 SichunHao sichunh@bu.edu

trans = 8.796e12
Me = 5.98e24
Mv = 0.065
Mh = 0.001
Mu = 0.285
mol=6.02e23
Nv = 13*mol*Me/Mv/trans 
Nmin = mol*Me/Mu/trans 
Nmax = 112*mol*Me/Mh/trans 

print("%e"%Nv)
print("%e"%Nmin)
print("%e"%Nmax)

