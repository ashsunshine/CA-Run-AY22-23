def get_nested_list(list_str):
    first_bracket = False
    first_nest = False
    inner_nests = 0
    nest_list = []
    digits = "1234567890"

    for ch in list_str:
        # triggers when the first bracket of the list is met
        if ch == "[" and not first_bracket:
            first_bracket = True
        
        # triggers when the first nested list bracket is met
        elif ch == "[" and not first_nest:
            first_nest = True
        
        # triggers when subsequent nested list opening brackets are met
        elif ch == "[" and first_nest:
            inner_nests += 1

        # triggers when closing bracket of subsequent nested list is met
        elif ch == "]" and inner_nests > 0:
            inner_nests -= 1
        
        # triggers when closing bracket of the first nested list is met, returns the nest_list
        elif ch == "]" and inner_nests == 0:
            return nest_list

        # triggers when the ch is a digit and the digit is in the first nested list.
        elif ch in digits and inner_nests == 0 and first_nest:
            nest_list.append(int(ch))
