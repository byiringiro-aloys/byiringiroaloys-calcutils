'''
operations.py
Core arithmetic and statistical helpers functions for calcutils
'''

'''
NOTE: This package for calculation utilities is limited to two numbers for calculations
'''

def add(num1:float,num2:float)->float:
    '''Return the sum of two numbers'''
    return num1+num2

def subtract(big_num1:float,small_num2:float)->float:
    '''Return the difference between two numbers'''
    return big_num1-small_num2

def multiply(num1:float,num2:float)->float:
    '''Return the product of two numbers'''
    return num1*num2

def divide(num1:float,num2:float)->float:
    '''Return the dividend of two numbers'''
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Error: Can not divide by Zero."

def average(numbers: list)->float:
    '''Return arithmetic mean of a list of numbers'''
    if not numbers:
        return 0.0
    return sum(numbers)/len(numbers)