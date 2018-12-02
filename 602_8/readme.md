
Assignment 9: Recursion: WordBrain Solver
EC602 Design by Software
Fall 2018

    1 Introduction
        1.1 Due Date
        1.2 Submission
        1.3 Group Size
        1.4 Points
        1.5 About wordbrain
    2 The assignment: wordbrainsolver
        2.1 More specifications
        2.2 Example
        2.3 Extra words
        2.4 Required imports
        2.5 Downloads
        2.6 Hints: suggested imports
    3 Evaluation
    4 Checker

1 Introduction

This assignment is a natural situation for recursion to be used.
1.1 Due Date

This assignment is due 2018-12-14 at 23:59:59 (one second before midnight)
1.2 Submission

You can submit here: wordbrainsolver submit link
1.3 Group Size

For this assignment, the maximum group size is 4.
1.4 Points

This assignment is worth 20 points, 10 points for each of the C++ and python parts.
1.5 About wordbrain

The smartphone app wordbrain is a puzzle game. The game presents users with a grid of letters, ranging in size 2x2 up to 5x5 and even larger.

Here is an example:

example puzzle

The user is given the pattern of word lengths. For this puzzle, the first word to be solved for is 7 letters, then the second word is 4 letters, and the final word is 5 letters.

The words must be spelled with adjacent letters, and as correct words are formed, the remaining letters drop down.

The game play is easier to understand if you have the app, so please download it and try it.
2 The assignment: wordbrainsolver

Your program will be given the filenames of two word lists, via the command-line, like this:

wordbrainsolver firstwordlist secondwordlist

or

python wordbrainsolver.py firstwordlist secondwordlist

The firstwordlist is a file containing a small word list, and the secondwordlist is a file containing a more comprehensive word list.

The reason for two word lists is that the puzzle answer is more likely to use basic words than exotic / rare words, so the result of the small word list will be much faster, and if it finds an answer, usually the correct answer.

Your program will read from standard input a description of a puzzle to solve, in the following format:

nchn
iaaw
bpom
atsn
**** ***** *** ****

The first lines represent the word grid, and the line with asterisks represent the words to solved for. [Any letters specified in this last line are already known.]

Your program will then print out all possible solutions to the puzzle using the first word list as the set of possible words.

If there are none, then all possible solutions using the second word list will be printed.
2.1 More specifications

    The program should output a period '.' on a new line at the conclusion of each puzzle solution, whether the puzzle had a solution or not.
    The output must be printed in sorted order. For this puzzle, using the provided word lists, the following should be printed:

snow panic man bath
.

    The user of your program can continue to enter puzzles to be solved, without limit.
    There is no limit to the puzzle size: the puzzle might be 1x1 or 10x10 or 331x331
    The program only exits when EOF (ctrl-D) is encountered, or the user enters an empty line.
    The puzzles entered will all be in valid formats.

Your program must be called wordbrainsolver.cpp or wordbrainsolver.py
2.2 Example

The result of running

wordbrainsolver small_word_list.txt large_word_list.txt <puzzles.txt >solutions.txt

or

python wordbrainsolver.py small_word_list.txt large_word_list.txt <puzzles.txt >solutions.txt

when puzzles.txt is

hee
oqr
sua
*** ******
yson
elnn
hnca
olab
***** ***** ******
nchn
iaaw
bpom
atsn
**** ***** *** ****
vanmo
ipveo
toarr
tsmed
miipb
**** ******* ******* *******
vanmo
ipveo
toarr
tsmed
miipb
p*** ******* ******* *******
yson
elnn
hnca
olab
***** holly ******

is that the output is redirected to the file solutions.txt and that output should be

hoe square
.
banes holly cannon
hones bally cannon
honey balls cannon
.
snow panic man bath
.
opts bedroom vampire vitamin
post bedroom vampire vitamin
pots bedroom vampire vitamin
stop bedroom vampire vitamin
.
post bedroom vampire vitamin
pots bedroom vampire vitamin
.
banes holly cannon
.

The program should exit on an empty line of input or EOF.
2.3 Extra words

The following words have been added to both word lists as they appear frequently in the game:

    tv
    keyring

2.4 Required imports

You must import sys in the following way for the python program:

from sys import argv

This will prevent errors resulting from using sys.stdin instead of input().
2.5 Downloads

    small_word_list.txt
    large_word_list.txt
    puzzles.txt
    solutions.txt

2.6 Hints: suggested imports

One solution we have uses the following imports:

import numpy as np
from collections import Counter
from sys import argv

3 Evaluation

Your program will be graded on

    correctness 40%
    efficiency 30%
    elegance 20%
    style 10%

4 Checker

The final version of the checker is posted:

    wordbrainsolver_checker.py

