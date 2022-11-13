age_list = [('Molly',25), ('Jett',13), ('Sage', 21), ('Ashley', 40), ('Sean', 31), ('Michelle',21)]

with open('./q2.txt','w') as output_file:
    for age_tuple in age_list:
        output_file.write(age_tuple[0] + " : " + str(age_tuple[1]) + " -> ")
        if age_tuple[1] > 30:
            output_file.write("OLD")
        else:
            output_file.write("YOUNG")
        output_file.write("\n")

