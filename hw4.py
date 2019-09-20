#Javier Diaz
#Prof Nauman
#CS 115 Lab
#03 October 2018

# I pledge my honor that I have abided by the Stevens Honor System

from cs115 import *

def pascal_row(n):
    ''' Takes a positive integer as an input and returns a list of the elements
       corresponding to that row '''
    if n == 0:
        return [1]
    else:
        return [1] + next_row(pascal_row(n-1)) + [1]

def pascal_triangle(n):
    ''' Takes a positive inter as an input and returns a list of lists with the
       values of all the rows up until n '''
    if n == 0:
        return [[1]]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]

def next_row(L):
    ''' Takes a list as an input and creates a new list for the following row '''
    if L == [1]:
        return []
    else:
        return [L[0] + L[1]] + next_row(L[1:])

def test_pascal_row():
    ''' Test the pascal_row function'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(5) == [1,5,10,10,5,1]
    assert pascal_row(2) == [1,2,1]
    assert pascal_row(3) == [1,3,3,1]

def test_pascal_triangle():
    ''' Test the pascal_row function'''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
