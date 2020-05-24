# addition.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
Run python autograder.py
"""
class Badtype(Exception): #take into account the error situations
    pass
    


def add(a, b):
    if type(a)!=int and type(a)!=float: #make sure a has a good type (int or float)
        raise Badtype()
    if type(b)!=int and type(b)!=float: #make sure b has a good type (int or float)
        raise Badtype()
    c=a+b #we give the result of the sum in c and return c

    return c
    