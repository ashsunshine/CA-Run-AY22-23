##
# Author : Stephen Pang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def transcribe_problematic_numlist(string): 
    # YOUR CODE GOES HERE

    return None

# DO NOT MODIFY THE CODE BELOW:
print('----Test Case 1----')
result = transcribe_problematic_numlist('[,,,,,]')
print("Expected: []" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = transcribe_problematic_numlist('aP,,#[&3,140B,23,,S2,20aa,34^]')
print("Expected: [3, 140, 23, 2, 20, 34]" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = transcribe_problematic_numlist(')JEODOE32sa[P3S;fA,,Doo2ew51,Sda1,!=-2fgg0,0]FSDWFSA')
print("Expected: [3, 251, 1, 20, 0]" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = transcribe_problematic_numlist('[OISDJFOIDS,,,IB1SO@OKOFEO]jhj')
print("Expected: [1]" )
print("Actual:   " + str(result))
print()