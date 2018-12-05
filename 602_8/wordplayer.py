#!/usr/bin/python
import sys
from itertools import combinations
from math import factorial
# Copyright 2018 SichunHao sichunh@bu.edu


# this function is taught by someone else
def selffind(sc, str2):
    temp = list(sc)
    for chacter in list(str2):
        try:
            temp.remove(chacter)
        except ValueError:
            return -1
    return 0


# ---------------load & sort dictionary---------------
words = open(sys.argv[1]).read().split()
wordn1 = {}
wordn2 = {}
for w in words:
    i = len(w)
    if i not in wordn1.keys():
        wordn1[i] = []
        wordn1[i].append(w)
        w = "".join(list(sorted(w)))
        wordn2[i] = []
        wordn2[i].append(w)
    else:
        wordn1[i].append(w)
        w = "".join(list(sorted(w)))
        wordn2[i].append(w)
# -------------input words------------------
while(True):
    try:
        temp = input().split()
        searchword = sorted(temp[0])
        n = int(temp[1])
        if (n == 0):
            break
    except EOFError:
        exit(0)

    # -----------------select cer  tain length--------------------
    x = []
    f1 = factorial(len(searchword))
    f2 = factorial(n)
    f3 = factorial(len(searchword) - n)
    lcombination = f1/f2/f3

    if n not in wordn2.keys():
        pass
    else:
        tempwordlist = wordn2[n]
        if (lcombination > len(tempwordlist)):
            sc = "".join(list(searchword))
            i = -1
            for str2 in tempwordlist:
                i = i+1
                if (selffind(sc, str2) != -1):
                    if wordn1[n][i] not in x:
                        x.append(wordn1[n][i])
        else:
            collection = combinations(searchword, n)
            for str1 in collection:
                word = "".join(tuple(str1))
                i = -1
                for str2 in tempwordlist:
                    i = i+1
                    if (word == str2):
                        if wordn1[n][i] not in x:
                            x.append(wordn1[n][i])

# ---------------------output-------------------------------
    x.sort()
    for i in x:
        print(i)
    print(".")
