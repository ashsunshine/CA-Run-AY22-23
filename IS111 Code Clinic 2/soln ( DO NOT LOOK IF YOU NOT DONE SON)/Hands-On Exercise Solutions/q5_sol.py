ninja_list = []

with open('bingo_book.txt','r') as bingo_book:
    for line in bingo_book:
        line = line.rstrip('\n')
        col = line.split(',')
        ninja_info = [] # ['Naruto Uzumaki','Konohagakure'...]
        for detail in col:
            ninja_info.append(detail)
        ninja_list.append(ninja_info) # [ ['Naruto Uzumaki'...], ['Sakura Haruno'...]]


#print(ninja_list)
name = input("Please enter a ninja's name: ")
name_components = name.split(" ")
new_name = ""
for comp in name_components:
    comp = comp[0].upper() + comp[1:].lower()
    new_name += comp + " "

new_name = new_name[:-1] # removes the extra space behind the name


found = False
for ninja in ninja_list:
    if ninja[0] == new_name:
        found = True
        print("These are the following details of the ninja:\n")
        print("Name:",ninja[0])
        print("Village:",ninja[1])
        print("Gender:",ninja[2])
        print("Description:",ninja[3])
        print("Status:",ninja[4])
        print("Signature Move:",ninja[5])
        if len(ninja) == 7:
            print()
            print("This ninja has deserted his or her village!")

if not found:
    print("Error: "+name+" not found!")


