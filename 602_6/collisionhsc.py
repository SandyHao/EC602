#!/usr/bin/env python
# Copyright 2018 SichunHao sichunh@bu.edu
import numpy as np
import sys
import math
from sys import argv
#comand line
cl = []
#judge commend line
try:
    if (len(argv) > 0):
        for k in range(len(argv)-1):
            k=k+1
            argv[k]=float(argv[k])
    else:
        exit(2)
except:
    exit(2)

for i in range(len(argv)-1):
    if (argv[i+1]>=0):
        cl.append(argv[i+1])
if (len(cl)==0):
    exit(2)
cl.sort()
cls=[]
for i in range(len(cl)):
    cls.append(cl[i])
#name
names = []
#x
xaxis = []
#y
yaxis = []
#Vx
vx = []
#Vy
vy = []
#store collision time
t=[]

#judge input
for textinput in sys.stdin:
    if textinput=='\n':
        exit(1)
    else:
        textdict=str.split(textinput)
        if (len(textdict)%5 == 0):
            try:
                number = int((len(textdict))/5)
                for j in range(number):
                    for i in range(1,5):
                        textdict[j*5+i] = float(textdict[j*5+i])
            except:
                exit(1)
        else: 
            exit(1)
        number = int((len(textdict))/5)
        for j in range(number):
            names.append(textdict[5*j])                   
            xaxis.append(textdict[5*j+1])
            yaxis.append(textdict[5*j+2])
            vx.append(textdict[5*j+3])
            vy.append(textdict[5*j+4])

time=0.0
index1=0
index2=0


def collisiontime():
    global time
    global index1
    global index2
    global a
    global b
    global c
    #get smallest collision time
    time=float('inf')
    l=len(xaxis)
    for j in range(l):
        for i in range(j+1,l):
            a=(vx[j]-vx[i])**2+(vy[j]-vy[i])**2
            b=2*(xaxis[j]-xaxis[i])*(vx[j]-vx[i])+2*(yaxis[j]-yaxis[i])*(vy[j]-vy[i])
            c=(xaxis[j]-xaxis[i])**2+(yaxis[j]-yaxis[i])**2-100
            d=b*b-4*a*c
            if a==0:
                if b!=0:
                    x0=-c/b
                    if x0>=0 and x0<time:
                        time=x0
                        index1=j
                        index2=i
            else:
                if ((xaxis[j]-xaxis[i])*(vx[j]-vx[i])+(yaxis[j]-yaxis[i])*(vy[j]-vy[i]))<0:
                    if (d>=0):
                        if d==0:
                            x0=-b/(2*a)
                            if x0>=0 and x0<time:
                                time=x0
                                index1=j
                                index2=i
                        else:
                            x1=(-b+math.sqrt(d))/(2*a)
                            x2=(-b-math.sqrt(d))/(2*a)
                            if x2<0:
                                if x1>=0 and x1<time:
                                    time=x1
                                    index1=j
                                    index2=i
                            elif x2>=0 and x2<time:
                                time=x2
                                index1=j
                                index2=i
    #print(time)
    collisionjudge()

def collisionjudge():
    global cl
    global xaxis
    global yaxis
    global vx
    global vy
    global time
    #compare with command line
    while (len(cl)>0):
        if (cl[0]<time):
            print(cls[0])
            update_xaxis_y(cl[0])
            for j in range(len(xaxis)):
                print(names[j],xaxis[j],yaxis[j],vx[j],vy[j])
            time=time-cl[0]
            timechange(cl[0])
            cutcl()
        else:
            update_xaxis_y(time)
            update_ball_velocity(index1, index2, time)
            timechange(time)
            collisiontime()            

def timechange(subt):
    global cl
    global time
    for i in range(len(cl)):
        cl[i] = cl[i]-subt
        
def cutcl():
    global cl
    global cls
    temp=[]
    for i in range(len(cl)-1):
        temp.append(cl[i+1])
    cl=temp
    temps=[]
    for i in range(len(cls)-1):
        temps.append(cls[i+1])
    cls=temps

def update_xaxis_y(tc):
    global xaxis
    global yaxis
    for j in range(len(xaxis)):                
        xaxis[j] = xaxis[j] + vx[j]*tc
        yaxis[j] = yaxis[j] + vy[j]*tc

def update_ball_velocity(index1, index2, time):
    global vx
    global vy
    j=index1
    i=index2
    if ((xaxis[j]-xaxis[i])*(vx[j]-vx[i])+(yaxis[j]-yaxis[i])*(vy[j]-vy[i])==0):
        pass
    else:
        vji=[(vx[j]-vx[i]), (vy[j]-vy[i])]
        rji=[(xaxis[j]-xaxis[i]), (yaxis[j]-yaxis[i])]
        vij=[(vx[i]-vx[j]), (vy[i]-vy[j])]
        rij=[(xaxis[i]-xaxis[j]), (yaxis[i]-yaxis[j])]
        p1=(vji[0]*rji[0]+vji[1]*rji[1])/(rji[0]*rji[0]+rji[1]*rji[1])
        p2=(vij[0]*rij[0]+vij[1]*rij[1])/(rij[0]*rij[0]+rij[1]*rij[1])
        vx[j]=vx[j]-p1*rji[0]
        vy[j]=vy[j]-p1*rji[1]
        vx[i]=vx[i]-p2*rij[0]
        vy[i]=vy[i]-p2*rij[1]


if len(xaxis)<=1:
    for i in range(len(cl)):
        update_xaxis_y(cl[i])
        print(cl[i])
        for j in range(len(xaxis)):
            print(names[j],xaxis[j],yaxis[j],vx[j],vy[j])
else:
    collisiontime()





