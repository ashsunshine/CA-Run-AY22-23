
def get_highest_score(name,file):
    highscore_dict = {}
    with open(file,'r') as input_file:
        for line in input_file:
            line = line.rstrip('\n')
            cols = line.split(' ')
            first_element = True
            dict_key = ""
            for col in cols:
                if first_element:
                    dict_key = col
                    highscore_dict[col] = 0
                    first_element = False
                else:
                    # Convert to integer
                    col = int(col)
                    if col > highscore_dict[dict_key]:
                        highscore_dict[dict_key] = col

        return highscore_dict[name]

# DO NOT MODIFY THE CODE BELOW
# If you are getting a "No such file or directory" error, ensure that you open the q1 folder directly in your VSC, instead of the entire resource folder.

print('----Test Case 1----')
result = get_highest_score('Dana','q1.txt')
print("Expected: 50" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_highest_score('Jennifer','q1.txt')
print("Expected: 50" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_highest_score('Kristin','q1.txt')
print("Expected: 90" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = get_highest_score('Meese','q1.txt')
print("Expected: 80" )
print("Actual:   " + str(result))
print()

