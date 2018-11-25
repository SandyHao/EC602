#!/usr/bin/python
from numpy import fft,convolve,ones
# Copyright 2018 SichunHao sichunh@bu.edu
#Write a python functionloudest_band(music,frame_rate,bandwidth) which returns a tuple (low,high,loudest) containing information about the loudest part of music.
#The input parameters are:
#music: an ndarray of shape (N,) representing a continuous time signal which has been digitized. You may assume that music is real, and so the Fourier Transform will be conjugate symmetric.
#frame_rate: the sampling rate that was used to sample music
#bandwidth: the width of the frequency band to be selected (the loudest band)
#The output parameters (low,high,loudest) are:
#low: the low end of the loudest frequency band in music
#high: the high end of the loudest frequency band in music
#loudest: a time signal extracted (filtered) from music which contains only the frequencies of music that are in the loudest band.
#The units of frame_rate, bandwidth, low, and high are all Hz.
def loudest_band(music,frame_rate,bandwidth):
    wave = fft.fft(music)
    n = len(wave)
    deltaf = frame_rate/n
    N = int(bandwidth/deltaf)
    c = ones(N)
    energy = list(convolve(abs(wave)**2,c,'valid'))
    i=energy.index(max(energy))
    
    low = i*deltaf
    high = low+bandwidth

    filtered = n*[0]
    filtered[i:i+N] = wave[i:i+N]
    filtered[-i-N+n:-i+n] = wave[-i-N+n:-i+n]
    loudest = fft.ifft(filtered)
    return low,high,loudest
