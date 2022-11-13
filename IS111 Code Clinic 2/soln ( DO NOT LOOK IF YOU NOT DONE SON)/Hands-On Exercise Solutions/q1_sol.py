# PART A 

def banned_words(banned_string,word_list):
    banned_words = []
    for word in word_list:
        if banned_string in word.lower():
            banned_words.append(word)

    return banned_words

# PART B
sentence = input("Please enter a sentence: ")
banned_string = input("Please enter a banned string: ")
word_list = sentence.split(' ')
alphabets = "qwertyuiopasdfghjklzxcvbnm"

new_word_list = []
for word in word_list:
    new_word = ""
    for ch in word:
        if ch.lower() in alphabets:
            new_word += ch
    
    new_word_list.append(new_word)

ban_list = banned_words(banned_string,new_word_list)

print("The following words are banned:")
for ban in ban_list:
    print(ban)

# PART C
def banned_words2(banned_list,word_list):
    banned_words = []
    for word in word_list:
        for ban in banned_list:
            if ban in word.lower():
                banned_words.append(word)
                break

    return banned_words

# PART C Program

sentence = input("Please enter a sentence: ")
banned_strings = input("Please enter banned strings: ")
word_list = sentence.split(' ')
banned_list = banned_strings.split(',')
alphabets = "qwertyuiopasdfghjklzxcvbnm"

new_word_list = []
for word in word_list:
    new_word = ""
    for ch in word:
        if ch.lower() in alphabets:
            new_word += ch
    
    new_word_list.append(new_word)

banned = banned_words2(banned_list,new_word_list)

print("The following words are banned:")
for ban in banned:
    print(ban)













print("===============TEST CASES FOR PART (A)====================")
print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
result = banned_words('sa',['them','call','lolling','sarah','hall','mimosa'])
print("Expected: ['sarah', 'mimosa']")
print("Actual  : " + str(result))
print()
print("Expected type of returned value: <class 'list'>")
print("Actual type of returned value  : " + str(type(result)))
print()
print("====================")
print()

# Test Case 2:

print("Test Case #2:")
print()
result = banned_words('lle',['paradox','omega','falafel'])
print("Expected: []")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 3:

print("Test Case #3:")
print()
result = banned_words('ras',[])
print("Expected: []")
print("Actual  : " + str(result))
print()
print("====================")
print() 

print("===============TEST CASES FOR PART (C)====================")
print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
result = banned_words2(['str','int','num'],['numbers','ontegers','marry','integer','string'])
print("Expected: ['numbers', 'integer', 'string']")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 2:

print("Test Case #2:")
print()
result = banned_words2(['ill','bor','hap','ness'],['happiness','prosperity','death','boredom','fairwill','illness'])
print("Expected: ['happiness', 'boredom', 'fairwill', 'illness']")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 3:

print("Test Case #3:")
print()
result = banned_words2(['lay','sar','choo'],[])
print("Expected: []")
print("Actual  : " + str(result))
print()
print("====================")
print() 

# Test Case 3:

print("Test Case #4:")
print()
result = banned_words2([],['lunatic','dongle','scent','horrible'])
print("Expected: []")
print("Actual  : " + str(result))
print()
print("====================")
print() 


