'''
Created on _______________________
@author:   _______________________
Pledge:    _______________________

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter,scorelist):
    '''takes as input a single letter string called letter and 
    a list where each element in that list is itself a list of
    the form [character, value] where character is a single
    letter and value is a number associated with that letter
    (e.g. it's scrabble score)'''
    if letter == '':
        return 0
    elif letter == scorelist[0][0]:
        return scorelist [0][1]
    else:
        return letterScore(letter,scorelist[1:])

def wordScore(S,scorelist):
    ''' take as input a string S which will have only lowercase letters,
       and the scorelist from above. Should return as output the
       scrabble score of that string'''
    if S == "":
        return 0
    else:
        return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)

def scoreList(Rack):
   """takes as input a Rack which is a list of lower-case letters and returns a
list of all of the words in the global Dictionary that can be made from those letters and the
score for each one. Specifically, this function returns a list of lists, each of which contains a
string that can be made from the Rack and its Scrabble score."""
    return map(lambda word: [word,wordScore(word,scrabbleScores)],list_of_words(Dictionary,rack))

def bestWord(rack):
    scorelist=scoreList(rack)
    if scorelist==[]:
        return['',0]
        
    return reduce(lambda x,y: x if x[1]>y[1] else y, scorelist)

def list_of_words(Dictionary,rack):
    
    return filter(lambda word: isPossible(word,rack),Dictionary)

def isPossible(word,rack):
    if word=='':
        return True
    if word[0] in rack:
        return isPossible(word[1:],remove(word[0],rack))
    return False
def remove(letter,rack):
    if letter=="":
        return []
    if letter==rack[0]:
        return rack[1:]                        
    
    return [rack[0]]+remove(letter,rack[1:])
def scoreList(rack):
    return map(lambda word: [word,wordScore(word,scrabbleScores)],list_of_words(Dictionary,rack))

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
    







    
