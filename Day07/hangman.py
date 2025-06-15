import random
import requests 
# This url is used and its response is stored as normal file response_words
url = 'https://www.mit.edu/~ecprice/wordlist.10000'
# print(requests.get(url)) this will give response 200
 
file = open('response_words', 'r')
line = file.readline()

str = ""
while line:
    # print(line.strip())
    str += " " + line.strip()
    line = file.readline()
file.close()

# print(str)
# print(str.split(" "))

list_of_words = str.split(" ")
# print(list_of_words[2])
# length = 5
def length_of_word():
    length = input("Enter the length of the word").strip()
    return length

length_call = length_of_word()
if (not length_call.isdigit()):
    print("Invalid choice, Enter proper number")
    if length_call.isdigit() and (int(length_call) > 25 or int(length_call) < 3):
        print("Enter the number in the range 3 and 24")
    length_call = length_of_word()
elif length_call.isdigit():
    if length_call.isdigit() and (int(length_call) > 25 or int(length_call) < 3):
        print("Enter the number in the range 3 and 24")
        length_call = length_of_word()

# length = length_of_word()
# list_of words_filtered = [ x for x in list_of_words if len(x) > 6]
# list_of_words_filtered = list_of_words
# random choice will also have k which gives the length of the words to be considered
filtered_list = [x for x in list_of_words if len(x) == int(length_call)]
choice = random.choice(filtered_list)
print(choice)
# print(type(choice))
print("_" * (len(choice)))
print(list("_" * (len(choice))))
print(list(choice))

choice_blank = list("_" * (len(choice)))
# choice_blank[0] = 'l'
# print("".join(choice_blank))
score = 100

while "".join(choice_blank) != choice and score != 0:
    letter = input("Enter the guess").strip().lower()
    number = 10 if int(length_call) < 14 else 5

    if letter in choice and letter not in choice_blank:
        indices = [i for i, letter_in_choice in enumerate(choice) if letter_in_choice == letter]
        # print(indices)
        for i in indices:
            choice_blank[i] = letter
        # print("".join(choice_blank))
    elif letter in choice_blank:
        print("Letter already guessed. Try guessing with other letters")
    elif letter not in choice:
        print("Oops wrong choice!")
        # print(number)
        score = score - number
    print(f"Your score right now: {score}")
    print(f"You have {score//number} turns left")
    print("".join(choice_blank))

if (score == 0):
    print("You loose the match")
elif "".join(choice_blank) == choice:
    print(f"You guessed the word as {choice} correctly, Your final score is {score}")



