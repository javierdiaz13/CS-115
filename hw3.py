'''
Created on September 26, 2018
@author: Javier Diaz
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 3

'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from cs115 import *

def giveChange(amount,coins):
    if amount == 0:
        return [0,[]]
    elif coins == [] or amount < 0:
        return [float("inf"),[]]
    else:
        use = giveChange(amount - coins[0], coins)
        lose = giveChange(amount, coins[1:])
        if use[0] < lose[0]:
            return [use[0] + 1, [coins[0]] + use[1]]
        else:
            return [lose[0], lose[1]]

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def wordsWithScore(dct, scores):
'''List of words in dct, with their Scrabble score.
Assume dct is a list of words and scores is a list of [letter,number]
pairs. Return the dictionary annotated so each word is paired with its
value. For example, wordsWithScore(Dictionary, scrabbleScores) should
return [['a', 1], ['am', 4], ['at', 2] ...etc...'''
     if dct == []:
        return []
    else:
        return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)

def wordCheck(word):
    "' takes a string as an input and splits it into a list'''
    if word == "":
       return []
    else:
        return [word[0]]+ wordCheck(word[1:])
    
def wordScore(word, scorelist):
    ''' takes a string and a list of letter scores and returns the total score of the word'''
    wordList = wordCheck(word)
    if word == "":
        return 0
    else:
        return letterScore(wordList[0], scorelist) + wordScore(word[1:], scorelist)

def letterScore(letter, scorelist):
    ''' takes a letter and a list of letter scores and returns the value of the letter'''
    temp = scorelist[0]
    if scorelist == []:
        return 0
    elif temp[0] == letter:
        return temp[1]
    else:
        return letterScore(letter, scorelist[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def take(n, L):
    '''Returns the list L[0:n].'''
    if n < 0 or len(L) == 0 or n > len(L)
        return []
    elif len(L) == 0:
        return []
    else:
        return [L[0]] + take(n-1, L[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def drop(n, L):
    ''' Returns the list L[n:]'''
    if n < 0 or len(L) == 0 or n > len(L):
        return []
    elif n != 0:
        return drop(n-1,L[1:])
    else: 
        return L
   
  
                        
     




