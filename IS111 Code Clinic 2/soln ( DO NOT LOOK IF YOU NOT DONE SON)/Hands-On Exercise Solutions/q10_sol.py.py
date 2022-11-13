def surround(field_list):
    # YOUR CODE GOES HERE
    for a in range (len(field_list)):
        if 'X' in field_list[a]:
            list_position = a

    for b in range (len(field_list[list_position])):
        if field_list[list_position][b] == 'X':
            x_position = b
    
    if list_position == 0: # no top
        if x_position != 0: 
            field_list[list_position][x_position-1] += 'O' # left
        if x_position != len(field_list[list_position])-1:
            field_list[list_position][x_position+1] += 'O' # right
        field_list[list_position+1][x_position] += 'O' # below

    elif list_position == len(field_list)-1: # no bottom
        if x_position != 0:
            field_list[list_position][x_position-1] += 'O' # left
        if x_position != len(field_list[list_position])-1:
            field_list[list_position][x_position+1] += 'O' # right
        field_list[list_position-1][x_position] += 'O' # top

    else: # everything
        if x_position != 0:
            field_list[list_position][x_position-1] += 'O' # left
        if x_position != len(field_list[list_position])-1:
            field_list[list_position][x_position+1] += 'O' # right
        field_list[list_position-1][x_position] += 'O' # top
        field_list[list_position+1][x_position] += 'O' # bottom

    return field_list