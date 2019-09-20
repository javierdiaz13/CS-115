# Javier Diaz
# Comp Sci
#Prof Nauman
# 22 October 2018

# I pledge my honor that I have abided by the Stevens Honor System

def isBase(N,B):
    ''' Checks if N is divisible by B'''
    if N % B != 0:
        return False
    else:
        return True

def numToBaseB(N,B):
    ''' that takes as input a non-negative (0 or larger)
integer N and a base B (between 2 and 10 inclusive) and returns a string representing the number N in
base B. (The rightmost digit of the string is the least significant digit of the number in base B.) Your code
should output the string '0' when the input value of N is 0.'''
    if N == 0:
        return "0"
    else:
        temp = numToBaseB(N//B,B) + str(N%B)
        return numToBaseBHelper(temp)

def numToBaseBHelper(S):
    '''''that takes as input a non-negative (0 or larger)
integer N and a base B (between 2 and 10 inclusive) and returns a string representing the number N in
base B. (The rightmost digit of the string is the least significant digit of the number in base B.) Your code
should output the string '0' when the input value of N is 0.'''
    if S == '':
        return ''
    elif S[0] != str(0):
        return S
    else:
        return numToBaseBHelper(S[1:])

def baseBToNum(S,B):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    accumulator = 0
    def baseBToNumHelper(S,B,accumulator):
        if S == '':
            return 0
        elif int(S[-1]) != 0:
            return baseBToNumHelper(S[:len(S)-1],B,accumulator + 1) + (B**accumulator)*int(S[-1])
        else:
            return baseBToNumHelper(S[:len(S)-1],B,accumulator + 1)
    return baseBToNumHelper(S,B,accumulator)    

def baseToBase(B1,B2,SinB1):
    ''' baseToBase(10, 2, "3") '''
    '''  takes three inputs: a base B1, a base B2 (both of which are
between 2 and 10, inclusive) and SinB1, which is a string representing a number in
base B1. baseToBase should return a string representing the same number in base B2'''
    return numToBaseB(baseBToNum(SinB1,B1),B2)

def add(S,T):
    ''' that takes two binary strings S and T as input and returns their sum, also in binary
        You can do this by converting the
two binary strings to two base-10 numbers, adding the two numbers, and then converting the resulting
sum back into base 2! Here is some sample input and output'''
    if S == '':
        return T
    elif T == '':
        return S
    else:
        return numToBaseB((int(baseToBase(2,10,S)) + int(baseToBase(2,10,T))),2)
    
FullAdder = {('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1')}

def addB(S1, S2):
    countBit= '0'
    sumBit='0'
    
    if min(S1,S2) == S1:
        S1 = addBHelper(S1, len(S2))
    else:
        S2 = addBHelper(S2, len(S1))
        
    def addB2(S1, S2, countBit):
            if len(S1) == 0:
                if countBit == "0":
                    return ''
                else:
                    return countBit
            else:
                sumBit, countBit = FullAdder[(S1[-1],S2[-1],countBit)]
                return addB2(S1[:len(S1)-1],S2[:len(S2)-1], countBit) + sumBit
    return addB2(S1,S2,countBit)

def addBHelper(S,length):
    if len(S) != length:
        S = '0' + S
        return addBHelper(S, length)
    else:
        return S

















    

