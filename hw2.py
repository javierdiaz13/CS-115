import sys
from cs115 import map, reduce, filter

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


def letterScore(letter, scoreList):
"""takes as input a single letter string called letter and
a list where each element in that list is itself a list of the form [character,
value] where character is a single letter andvalue is a number associated with that letter
(e.g. it's scrabble score)."""
    if scoreList==[]:
        return 0
    elif scoreList[0][0]==letter:
        return scoreList[0][1]
    else:
        return letterScore(letter,scoreList[1:])

def bestWord(rack):
'''takes as input a Rack as above and returns a list with two elements: the
highest possible scoring word from that Rack followed by its score'''
    scorelist=scoreList(rack)
    if scorelist==[]:
        return['',0]
    else:
        return reduce(lambda x,y: x if x[1]>y[1] else y, scorelist)

def wordScore(S,scoreList):
"""should take as input a string S and a scorelist in the format
described above, which will have only lowercase letters, and should return as output the
scrabble score of that string"""
    if S=="":
        return 0
    else:
        return letterScore(S[0],scoreList) + wordScore(S[1:],scoreList)
    
def scoreList(rack):
"""takes as input a Rack which is a list of lower-case letters and returns a
list of all of the words in the global Dictionary that can be made from those letters and the
score for each one"""
    return map(lambda word: [word,wordScore(word,scrabbleScores)],wordList(Dictionary,rack))

def wordList(Dictionary,rack):
    '''returns a list of all pssible wordsthat can be made'''
     return filter(lambda word: isPossible(word,rack),Dictionary)

def isPossible(word,rack):
    '''inputs a word and list. returns true or false whether a word from the list can be made'''
    if word=='':
        return True
    elif word[0] in rack:
        return isPossible(word[1:],removeElement(word[0],rack))
    else:
        return False

def removeElement(letter,rack):
    '''inputs a string and a list, removes an element from the list'''
    if letter=="":
        return []
    elif letter==rack[0]:
        return rack[1:]
    else:
        return [rack[0]]+removeElement(letter,rack[1:])


