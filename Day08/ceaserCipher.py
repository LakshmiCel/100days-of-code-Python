alphabets = []
for letter in range(ord('A'), ord('Z') + 1):
    # print(chr(letter))
    alphabets.append(chr(letter).lower())
proceed = 'start'
print("Welcome to ceaser cipher", "The process of encrypting the messages and decrypting them", "to make unintended person understanding the intent of the message", sep ="\n")
while(proceed in ('start', 'y')):
    def ask_proceed():
        proceed = input("\nEnter `y` to proceed or `n` to exit").strip().lower()
        if(proceed == 'n'):
            exit()
        elif(proceed not in ('y')):
            proceed = print("\n Invalid choice.", end=" ")
            ask_proceed()
    if(proceed != 'start'):
        ask_proceed()
    input_str = ""
    turns = 0
    def encrpt_decrypt(action, str, turns):
        for each_letter in str:
            if (action == 'encrypt'):
                # print(each_letter in alphabets, each_letter)
                if each_letter in alphabets:
                    index = (alphabets.index(each_letter) + turns)
                    order_value = 26 - index if(index >= 26) else index
                    # print(index, order_value)
                    print(alphabets[order_value], end="")
            elif (action == 'decrypt'):
                if each_letter in alphabets:
                    index = (alphabets.index(each_letter) - turns)
                    order_value = 26 + index if(index < 0) else index
                    # print(index, order_value)
                    print(alphabets[order_value], end="")
    def ask_action():
        action = input("\nEnter `encrypt` or `decrypt` to start the process").strip().lower()
        # print(action)
        if(action not in ('encrypt','decrypt')):
            ask_action()
        return action
    def ask_input():
        global action
        # action = ask_action()
        global input_str, turns
        input_str = input(f"Enter the text you need to {action}").strip()
        turns = int(input(f"Enter the rotations for the {action}ion"))
        
    action = ask_action()
    ask_input()
    # input_str, turn = ask_input()
    # print(type(input_str), input_str, turns , type(turns))
    encrpt_decrypt(action, input_str, turns)
    proceed = 'y'

