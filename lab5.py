'''
Created on 04 October 2018
@author:  Javier Diaz
Pledge:    I pledge that I have abided by the Stevens Honor System

CS115 - Lab 5
'''
import time
from cs115 import map

words = []
HITS = 10

memo = {}

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    if (first,second) in memo:
        return memo[(first,second)]
    elif first == '':
        return len(second)
    elif second == '':
        return len(first)
    elif first[0] == second[0]:
        answer = fastED(first[1:], second[1:])
        memo[(first,second)] = answer
        return answer
    else:
        substitution = 1 + fastED(first[1:], second[1:])
        deletion = 1 + fastED(first[1:], second)
        insertion = 1 + fastED(first, second[1:])
        answer = min(substitution,deletion,insertion)
        memo[(first,second)] = answer
    return answer

def getSuggestions(user_input):
    return map(lambda x: (fastED(user_input,x),x),words)

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
