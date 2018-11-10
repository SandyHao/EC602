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
#The function loudest_band should be defined in an importable python file loudest.py.