word = input("Enter a palindrome: ")
is_palindrome = False

while not is_palindrome:
    if word == word[::-1]:
        is_palindrome = True
    else:
        word = input("That is not a palindrome, enter a palindrome! : ")

print("Finally, you entered a palindrome")