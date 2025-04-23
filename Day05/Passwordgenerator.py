# passwd generator with letter - Uppercase , lowercase, digits , punctuations
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
    digits.append(number)

#shuffling the lists 
random.shuffle(lowercase_letters)
random.shuffle(punctuations)
random.shuffle(digits)
random.shuffle(uppercase_letters)

# print(lowercase_letters)
# print(punctuations)
# print(digits)
# print(uppercase_letters)

# default_size = 10
size = 0
def ask_size():
    global size
    print("Welcome to passpy, We generate the random password")
    skip = input("Enter 1 to skip and the generate the 10 character password").strip()
    print(skip)
    if skip == '1':
        size = 10
    elif skip != '1':
        size_input = input("Enter the length of he password to be generated")
        if (not size_input.isdigit()):
            print("\nInvalid number , Please enter the number to help with password length")
            ask_size()
        size = int(size_input)
ask_size()

# Easy level where the passwd will have random sequence   
for step in range(1, size + 1):
    password += random.choice(lowercase_letters + uppercase_letters + digits + punctuations)
print("Your password is ready:", password)
    


