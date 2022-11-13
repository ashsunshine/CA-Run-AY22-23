def get_alpha_num(string):
    new_str = ""
    new_num = 0
    neg_check = False
    numbers = "1234567890"
    alphabets = "qwertyuiopasdfghjklzxcvbnm"
    for ch in string:


        # if previous ch was "-" but the next ch is NOT an integer
        if neg_check and ch not in numbers:
            neg_check = False

        # Checks if there is a negative symbol
        if ch == "-":
            neg_check = True

        # If ch is an integer when the previous ch was a '-'symbol
        elif ch in numbers and neg_check:
            new_num -= int(ch)
            neg_check = False

        # if ch is an integer but the previous ch was NOT a '-' symbol.
        elif ch in numbers and not neg_check:
            new_num += int(ch)

        # if ch is an alphabet
        elif ch.lower() in alphabets:
            new_str += ch


    return (new_str , new_num)

