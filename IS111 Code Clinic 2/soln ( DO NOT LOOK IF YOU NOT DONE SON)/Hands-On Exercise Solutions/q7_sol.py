## PART A
def add_receipient(email, receipient_list):
    receipient_list.append(email)
    return receipient_list

## PART B
prompt = "I'm crazy" # This is just a placeholder to get into the while loop.
receipient_list = []
while prompt != "no":
    email = input("Enter an email address: ")

    # Validate Email
    while ('@' not in email or email.count('@') > 1):
        print("Please enter a valid email address!")
        email = input("Enter an email address: ")

    receipient_list = add_receipient(email,receipient_list)

    prompt = input("\nDo you want to add more receipients? [yes or no] ")

    while not (prompt == "yes" or prompt == "no"):
        print("Please enter a valid response!")
        prompt = input("Do you want to add more receipients? [yes or no] ")

msg = input("\nPlease enter a message to send your receipients: ")
while msg == "":
    print("Your message cannot be empty!")
    msg = input("Please enter a message to send your receipients: ")


print("Your message, '"+ msg + "' has been sent to the following users:\n")
count = 1
for name in receipient_list:
    print(str(count) + ". " + name)
    count += 1

    
