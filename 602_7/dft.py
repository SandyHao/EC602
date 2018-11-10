from numpy import zeros, exp, array, pi
# Copyright 2018 SichunHao sichunh@bu.edu

#Write a python function dft(x) which returns the DFT of a sequence of complex numbers. 
#the function dft must return a numpy.ndarray with shape (N,) and this returned value should match the definition of the DFT provided in this assignment
#the function dft must raise a ValueError exception if the input value x is not a sequence of numerical values
#x[n] for a sequence x[0],x[1],x[2]
#s[n]=s(nτ)Sampling is done by storing the signal s(t) at regular times spaced by τ seconds, where τ is called the sampling interval.
#fs=1/τ   frequencies f up to fs/2 are correctly recorded.

def dft(x):
    try:
        N=len(x)
        m=[]
        X=[]
        for n in range(N):
            m.append(complex(x[n]))
            X.append(complex(0,0))
    except:
        raise ValueError

    for k in range(N):
        for n in range(N):
            X[k] += m[n].real*(exp(-1j*2*pi*n*k/N))+m[n].imag*1j*(exp(-1j*2*pi*n*k/N))

    X=array(X)
    return X
