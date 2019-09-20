'''
Created on: October 17, 2018
@author:    Javier Diaz
Pledge:     "I pledge my honor that I have abided by the Stevens Honor System" 

CS115 - Hw 6

Got help from CS115 tutor!
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False
    return True

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n // 2) + '1'
    return numToBinary(n // 2) + '0'
      
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif int(s[-1]) == 1:
        return 1 + (2 * binaryToNum(s[:-1]))
    return 2 * binaryToNum(s[:-1])
    
t = 0 
def compress(s):
    '''This function  takes a binary string of length 64 and
    returns a binary string that represents the amount of 
    consecutive 0s and 1s that are in the sequence. The output 
    is also alternating between amount 0s and 1s '''
    global t
    if s == '' or s == []:
        t = 0
        return ''
    elif t == 0:
        t += 1
        s = compress_helper(s)
        return compress(s)
    elif s[0] >= MAX_RUN_LENGTH + 1:
        s[0] = s[0] - (MAX_RUN_LENGTH)
        t += 1                     
        return str(numToBinary(MAX_RUN_LENGTH)) + '0' * COMPRESSED_BLOCK_SIZE + compress(s)      
    else:
        t += 1                                  
        return bin_to_bits(str(numToBinary(s[0]))) +  compress(s[1:])
    
def bin_to_bits(S):
    '''This function takes in the string from compress(S) and outputs
    the zeros remaining to finish the (COMPRESSED_BLOCK_SIZE - 1) bit size of 5'''
    if len(S) != (COMPRESSED_BLOCK_SIZE):
        return '0' * ((COMPRESSED_BLOCK_SIZE) -len(S)) + S
    return S
    
i = 0
def compress_helper(S):
    '''This function takes in a string from compress(S) and outputs
    a list of the amount of zeros and ones consecutively'''
    global i
    if S == '':
        i = 0
        return []
    else:
        if isOdd(i) == 0:
            i += 1
            return [find_zero(S)] + compress_helper(next_one(S))
        else:
            i += 1
            return [find_one(S)] + compress_helper(next_zero(S))
    
def find_zero(S):
    '''This function takes in a string which counts how many zeros there are
    starting from the left up until the first encounter of a one and outputs the result'''
    if S == '':
        return 0
    elif S[0] == '0':
        return 1 + find_zero(S[1:])
    return 0

def find_one(S):
    '''This function takes in a string S which counts how many ones there are
    starting from the last zero up until the next zero and outputs the result'''
    if S == '':
        return 0
    elif S[0] == '1':
        return 1 + find_one(S[1:])
    return 0
   
def next_zero(S):
    '''This function takes in a string S which outputs the next consecutive zeros '''
    if S == '':
        return ''
    elif S[0] == '1':
        return next_zero(S[1:])
    return S
 
def next_one(S):
    '''This function takes in a string S which outputs the next consecutive ones'''
    if S == '':
        return ''
    elif S[0] == '0':
        return next_one(S[1:])
    return S

def uncompress(S):
    '''This function takes in compressed string S and outputs the uncompressed
    string back to its original state'''
    outer_loop = False
    global t
    if t == 0:
        outer_loop = True
        t = 1
    if S == '':
        t = 0
        return []
    else:
        S = [binaryToNum(S[0:COMPRESSED_BLOCK_SIZE])] + uncompress(S[COMPRESSED_BLOCK_SIZE:])
        if(not outer_loop):
            return S
    if outer_loop:
        return uncompress_helper(S)
    
def uncompress_helper(L):
    '''This function takes in a list L from the function uncompress and outputs
    the final string of binary numbers to its original uncompressed state.'''
    global i
    if L == []:
        i = 0
        return ''
    elif isOdd(i) == 0: 
        i += 1
        return '0' * L[0] + uncompress_helper(L[1:])
    else: 
        i += 1
        return '1' * L[0] + uncompress_helper(L[1:])

def compression(S):
    '''This function takes in a string S and outputs the ratio of the length of
    the compressed string to the original string'''
    return len(compress(S)) / len(S)
