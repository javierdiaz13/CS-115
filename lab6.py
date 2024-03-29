'''
Created on 11 October 2018
@author:   Javier Diaz
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    ''' 101010  42'''
    if n % 2 == 1:
        return True
    else:
        return False

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n <= 0:
        return ""
    elif isOdd(n):
        return numToBinary(n//2) + "1"
    else:
        return numToBinary(n//2) + "0"
        

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    accumulator = 0
    def btn_helper(s,accumulator):
        if s == "":
            return 0
        elif int(s[-1]) == 1:
           return btn_helper(s[:len(s)-1], accumulator + 1) + 2**accumulator
        else:
           return btn_helper(s[:len(s)-1], accumulator + 1)
    return btn_helper(s, accumulator)
                           

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    temp = str(numToBinary(binaryToNum(s)+1))
    temp2 = (len(s)-len(temp))*"0" + temp
    if len(temp2) != 8:
        return temp2[1:]
    else:
        return temp2
    

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n < 0:
        return " "
    else:
        print(s)
        count(increment(s),n-1)
        

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n <= 0:
        return ""
    elif n % 3 == 0:
        return numToTernary(n//3) + "0"
    elif  n % 3 == 1:
        return numToTernary(n//3) + "1"
    else:
        return numToTernary(n//3) + "2"

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    accumulator = 0
    def ttn_helper(s,accumulator):
        if s == "":
            return 0
        elif int(s[-1]) == 1:
           return ttn_helper(s[:len(s)-1], accumulator + 1) + 3**accumulator
        elif int(s[-1]) == 2:
            return ttn_helper(s[:len(s)-1], accumulator + 1) + 2*(3**accumulator)
        else:
           return ttn_helper(s[:len(s)-1], accumulator + 1)
    return ttn_helper(s, accumulator)
