def create_prime_dict(num_list):
    # YOUR CODE GOES HERE

    return None

# DO NOT MODIFY THE TEST CASES BELOW
print('----Test Case 1----')
result = create_prime_dict([2, 3, 5, 10, 20, 23])
print("Expected: {2: True, 3: True, 5: True, 10: False, 20: False, 23: True}" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = create_prime_dict([4, 5, 6, 8, 11, 12])
print("Expected: {4: False, 5: True, 6: False, 8: False, 11: True, 12: False}" )
print("Actual:   " + str(result))
print()