import numpy as np
import scipy
import wave
import math
from math import cos
from scipy.io.wavfile import write
from IPython.display import Audio
from numpy import zeros, exp, array, pi
# Copyright 2018 SichunHao sichunh@bu.edu
# Write a python function dialer(file_name,frame_rate,phone,tone_time) which creates a WAV file of the sound of a telephone number being dialed.
# The parameters are
# file_name, a string representing the name of the WAV file to be created. Do not append ".wav" to this string.
# frame_rate, a number representing the number of samples per second to use in the sound：
    #The sampling rate or sampling frequency 
    #fs=1/τ determines the range of frequencies that can be recorded from the original based on the Nyquist Theorem: 
    #frequencies f up to fs/2 are correctly recorded.
# phone, a string of digits representing a phone number to dial.
# tone_time, a number representing the time in seconds of each tone to generate.
# The function dialer should be defined in an importable python file dialer.p

def dialer(file_name,frame_rate,phone,tone_time):
    npoints = int(frame_rate*tone_time)
    t = np.linspace(0,tone_time,npoints)
    tone = []
    times = int(tone_time*frame_rate)
    l = tone_time/times
    x=0
    i=0
    for a in phone:
        t = tone_time*i
        i=i+1
        for j in range(times):
            x = j*l         
            v = calcucos(a,t,x)
            tone.append(v)
    tone = array(tone)
    print(tone)
    write(file_name, frame_rate, tone)

def calcucos(a,t,x):
    if a=='0':
        b=cos(2*pi*(t+x)*941)+cos(2*pi*(t+x)*1477)
    elif a=='1':
        b=cos(2*pi*(t+x)*697)+cos(2*pi*(t+x)*1209)
    elif a=='2':
        b=cos(2*pi*(t+x)*697)+cos(2*pi*(t+x)*1336)
    elif a=='3':
        b=cos(2*pi*(t+x)*697)+cos(2*pi*(t+x)*1477)
    elif a=='4':
        b=cos(2*pi*(t+x)*770)+cos(2*pi*(t+x)*1209)
    elif a=='5':
        b=cos(2*pi*(t+x)*770)+cos(2*pi*(t+x)*1336)
    elif a=='6':
        b=cos(2*pi*(t+x)*770)+cos(2*pi*(t+x)*1477)
    elif a=='7':
        b=cos(2*pi*(t+x)*852)+cos(2*pi*(t+x)*1209)
    elif a=='8':
        b=cos(2*pi*(t+x)*852)+cos(2*pi*(t+x)*1336)
    elif a=='9':
        b=cos(2*pi*(t+x)*852)+cos(2*pi*(t+x)*1477)
    return b

dialer('firsttry',8000,'01',0.1)
