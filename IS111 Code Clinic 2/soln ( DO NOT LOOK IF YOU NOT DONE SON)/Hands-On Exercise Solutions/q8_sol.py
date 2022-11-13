weapons_dict = {
    "kunai": 5,
    "shuriken": 20,
    "hammer": 2,
    "spiked ball": 24,
    "metal spear": 4,
    "senbon": 84,
    "six-edged disc": 42,
    "crossbow": 1,
    "dual-swords": 3,
    "kunai chains": 2,
    "iron fan": 5,
    "scythe": 9,
    "scimitar": 12
}

action = input("What would you like to do? [take/add] ")
while not (action == "take" or action == "add"):
    action = input("Please enter a valid action [take/add]: ")

weapon = input("Enter the name of the weapon: ")

# if action is 'take'
if action == "take":
    while (weapon not in weapons_dict):
        print("\nWeapon not found in stocks!")
        weapon = input("Enter another weapon: ")
    print()
    num = int(input("Enter the number of weapons you would like to take: "))
    
    while (num > weapons_dict[weapon]):
        print("The amount of weapons you are trying to take exceeds what you have already!")
        num = int(input("Enter the number of weapons you would like to take: "))

    weapons_dict[weapon] -= num

    if (weapons_dict[weapon] == 0):
        print("\nYou have no more "+ weapon +" left in the stocks.")
    else:
        print("\nYou are left with "+ str(weapons_dict[weapon]) +" of the following weapon: "+ weapon)

if action == "add":
    num = int(input("Enter the number of weapons you would like to add to the stocks: "))
    if weapon not in weapons_dict:
        weapons_dict[weapon] = num
    else:
        weapons_dict[weapon] += num
    
    print("You now have a total of " + str(weapons_dict[weapon]) + " "+ weapon + " left in the stock.")

