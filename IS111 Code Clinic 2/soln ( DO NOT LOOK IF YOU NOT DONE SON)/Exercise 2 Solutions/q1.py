def get_factorial(n):
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    
    return answer


# DO NOT MODIFY THE CODE BELOW
print('----Test Case 1----')
result = get_factorial(5)
print("Expected: 120" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_factorial(8)
print("Expected: 40320" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_factorial(4)
print("Expected: 24" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = get_factorial(10)
print("Expected: 3628800" )
print("Actual:   " + str(result))
print()