##
# Author : Stephen Pang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def decode_calculate(string):
    # YOUR CODE GOES HERE

    return None

# DO NOT MODIFY THE CODE BELOW:
print('----Test Case 1----')
result = decode_calculate('aS-3o5AkE2b05#6')
print("Expected: ('aSoAkEb#', 15)" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = decode_calculate('@kaNsaShiRo')
print("Expected: ('@kaNsaShiRo', 0)" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = decode_calculate('-25010245-35-92')
print("Expected: ('', 10)" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = decode_calculate('s-5A-N--8cHa2---Na')
print("Expected: ('sA-N-cHa---Na', -11)" )
print("Actual:   " + str(result))
print()