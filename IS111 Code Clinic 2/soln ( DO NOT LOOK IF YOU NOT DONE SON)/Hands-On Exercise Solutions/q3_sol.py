def compute_steps(up,down,left,right):
    vertical = up - down
    # turns vertical into a postiive integer
    if vertical < 0:
        vertical = -vertical
    
    # turns horizontal distance into a positive integer
    horizontal = left - right
    if horizontal < 0:
        horizontal = -horizontal

    # print(horizontal)
    # print(vertical)
    distance = round((horizontal**2 + vertical**2) ** (1/2),2)

    # checking if the distane is a float or a integer
    distance = str(distance)
    distance_list = distance.split(".") # Gives a list of 2 elements, with the 2nd element being the decimal points.

    if distance_list[1] == "0":
        return distance_list[0]
    else:
        return distance


# Since the question did not specify for distance to be in string/float/integer type, you may keep it in string form.