def get_letter_count_dict(string):
    letter_count_dict = {}
    for ch in string:
        ch = ch.lower() # convert to lowercase
        if ch not in letter_count_dict:
            letter_count_dict[ch] = 1
        else:
            letter_count_dict[ch] += 1 #

    return letter_count_dict


# DO NOT MODIFY THE CODE BELOW
print('----Test Case 1----')
result = get_letter_count_dict('Annabella')
print("Expected: {'a': 3, 'n': 2, 'b': 1, 'e': 1, 'l': 2}" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_letter_count_dict('poltergeist')
print("Expected: {'p': 1, 'o': 1, 'l': 1, 't': 2, 'e': 2, 'r': 1, 'g': 1, 'i': 1, 's': 1}" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_letter_count_dict('huiQingLing')
print("Expected: {'h': 1, 'u': 1, 'i': 3, 'q': 1, 'n': 2, 'g': 2, 'l': 1}" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = get_letter_count_dict('nicoleSeATTle')
print("Expected: {'n': 1, 'i': 1, 'c': 1, 'o': 1, 'l': 2, 'e': 3, 's': 1, 'a': 1, 't': 2}" )
print("Actual:   " + str(result))
print()