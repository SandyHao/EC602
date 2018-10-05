#!/usr/bin/env bash
#Copyright 2018 SichunHao sichunh@bu.edu
g++ fourargs.cpp -o fourargs
python fourargs.py 1 2 3 4 5 6
python fourargs.py 1 2 3
fourargs 1 two 3 4 5 6
fourargs one two 3