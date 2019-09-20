from cs115 import map, reduce
import math

#Javier Diaz
#I pledge my honor that I have abided by the Stevens Honor System

def add(x,y):
    '''takes two integers as an input and adds them'''
    return x+y

def multiply(x,y):
    '''takes two integers as an input and multiplies them'''
    return x*y

def factorial(n):
    '''takes an integer as an input and returns its factorial'''
    return reduce(multiply,range(1,n+1))

def mean(L):
    '''takes a list as an input and returns the average'''
    return (reduce(add,L))/len(L)

def divides(n):
    '''Takes two integer inputs and checks if they are divisible'''
    def div(k):
        return n % k == 0
    return div

def prime(n):
    '''takes an integer as an input and checks if it is prime'''
    return (reduce(add,map(divides(n),range(1,n+1)))) == 2
