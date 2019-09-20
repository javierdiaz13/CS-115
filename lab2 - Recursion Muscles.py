from cs115 import *
import math

#Javier Diaz
#I pledge my honor that I have abided by the Stevens Honor System


def mylen(L):
    if L == [] or L == "":
        return 0
    else:
        return 1 + mylen(L[1:])
    
def dot(L,K):
    '''Takes two lists as input and sums of the products of corresponding cells'''
    if L==[] or K==[]:
        return 0
    else:
        return L[0]*K[0] + dot( L[1:] , K[1:] )

def explode(s):
    '"Takes a string as an input and return all of its characters in a list'''
    if s == "":
       return []
    else:
        return [s[0]] + explode(s[1:])
    
def ind(e,L):
    '''Takes an element and list/string as an input and returns the index of e in L'''
    if L == [] or L == "":
        return mylen(L)
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e,L[1:])

def removeAll(e,L):
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e,L[1:])
    else:
        return [L[0]] + removeAll(e,L[1:])
    
def f(x):
    if x % 2 == 0 :
        return True
    else:
        return False

def myFilter(f,L):
    if L== []:
        return []
    elif f(L[0]) == True:
        return [L[0]] + myFilter(f,L[1:])
    else:
        return myFilter(f,L[1:])

def deepReverse(L):
        if L == []:
            return []
        elif isinstance(L[0], list):
            return deepReverse(L[1:]) +[deepReverse(L[0])]
        else:
            return deepReverse(L[1:]) + [L[0]] 





        
        
