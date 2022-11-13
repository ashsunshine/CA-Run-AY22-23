# PART A
def binary_to_music(binary_code):
    music_string = ""
    music_binary_dict = {'000': 'C', '001': 'D', '010': 'E', '011' : 'F', '100': 'G', '101' : 'A', '110' : 'B'}
    for i in range(0,len(binary_code),3):
        binary_note = binary_code[i:i+3]
        music_note = music_binary_dict[binary_note]
        music_string += music_note

    return music_string



# PART B

def binary_to_music2(binary_code):
    music_string = ""
    music_binary_dict = {'000': 'C', '001': 'D', '010': 'E', '011' : 'F', '100': 'G', '101' : 'A', '110' : 'B'}

    while (binary_code != ""):
        binary_note = binary_code[0:3] # takes in the first 3 digits at the front.
        found = False
        for binary in music_binary_dict:
            if binary == binary_note:
                found = True
                music_note = music_binary_dict[binary_note]
                music_string += music_note
                if len(binary_code) <= 3:
                    binary_code = ""
                else:
                    binary_code = binary_code[3:]

        if not found:
            binary_code = binary_code[0:2] + binary_code[3:] # removes the 3rd number, which is fake

    return music_string


        