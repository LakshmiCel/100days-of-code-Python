# Hard level where the sequence is determined and the digits and everything is userdefined 

import random
lowercase_letters = []
uppercase_letters = []
digits = []
punctuations = ['!', '@', '#', '$', '%', '^', '&', '*']
password = ""
for letter in range(ord('A'), ord('Z') + 1):
    # print(chr(i).lower())
    lowercase_letters.append(chr(letter).lower())
    uppercase_letters.append(chr(letter))
# print(lowercase_letters)
# print(uppercase_letters)

for number in range(0, 10):
    digits.append(str(number))

#shuffling the lists 
random.shuffle(lowercase_letters)
random.shuffle(punctuations)
random.shuffle(digits)
random.shuffle(uppercase_letters)

lowercase_length = 0
uppercase_length = 0
digits_length = 0
special_characters_length = 0

size = 0
def ask_input():
    global size
    size_input = input("Enter the number of password to be generated").strip()
    if (not size_input.isdigit()):
        print("\nInvalid number , Please enter the number to help with password length")
        ask_input()
    size = int(size_input)

def ask_for_each_type_length():
    ask_input()
    global special_characters_length, lowercase_length, uppercase_length, digits_length
    lowercase_length = int(input("Enter the number of lowercase letters required in password: ").strip())
    uppercase_length = int(input("Enter the number of uppercase letters required in password: ").strip())
    digits_length = int(input("Enter the number of digits required in password: ").strip())
    special_characters_length = int(input("Enter the number of special characters required in password: ").strip())
    if ((lowercase_length + uppercase_length + digits_length + special_characters_length) != size):
        print(f" Password size of {size} doesnt match with the total size of password for different types {lowercase_length + uppercase_length + digits_length + special_characters_length}")
        print(" Try lowering the total password of each type or increasing the size of the password "if (lowercase_length + uppercase_length + digits_length + special_characters_length > size) else " Try increasing the size of each character type length or decreasing the size of the password")
        ask_for_each_type_length()
    # return lowercase_length, uppercase_length, digits_length, special_characters_length

def generate_password():
    global lowercase_letters, uppercase_letters, digits, punctuations, special_characters_length, lowercase_length, uppercase_length, digits_length
    ask_for_each_type_length()
    # lowercase_length, uppercase_length, digits_length, special_characters_length = ask_for_each_type_length()
    print(lowercase_length, uppercase_length, digits_length, special_characters_length)

    lowercase = ''.join(random.choices(lowercase_letters, k=lowercase_length))
    uppercase = ''.join(random.choices(uppercase_letters, k=uppercase_length))
    digits = ''.join(random.choices(digits, k=digits_length))
    special_characters = ''.join(random.choices(punctuations, k=special_characters_length))
    password = lowercase + uppercase + digits + special_characters
    return ''.join(random.sample(password, len(password)))
# print("Generated Password:", password)
password = generate_password()
print("Your password is ready:", password)

    
