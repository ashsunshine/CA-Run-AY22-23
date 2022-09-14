##
# Author : Stephen Pang
# Created : July 31, 2021
# Last Updated : July 31, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def isFactor(num,factor):
    # YOUR CODE GOES HERE

    return None

# DO NOT MODIFY THE CODE BELOW
print('----Test Case 1----')
result = isFactor(5,2)
print("isFactor(5,2)")
print("Expected Type: <class 'bool'>")
print("Expected: False" )
print("Actual:   " + str(result))
print("Actual Type: " + str(type(result)))
print()
print('----Test Case 2----')
result = isFactor(30,2)
print("isFactor(30,2)")
print("Expected Type: <class 'bool'>")
print("Expected: True" )
print("Actual:   " + str(result))
print("Actual Type: " + str(type(result)))
print()
print('----Test Case 3----')
result = isFactor(100,0)
print("isFactor(100,0)")
print("Expected: None" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = isFactor(45,1)
print("isFactor(45,1)")
print("Expected: None" )
print("Actual:   " + str(result))
print()