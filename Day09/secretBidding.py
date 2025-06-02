import random
# bid_amount = 0
winner = {}
start = 'yet'

rules_list = ["At the moment, only on bid can be made", "Once started the bid has to end completely for a new bid to start",
"If the bid has already begun, the concurrent entries will continue to add up on the same bid",
"Some bids can have initial quote as well, which will be know at bid initiation", 
"Once the last person call it quits, the winner will be decided. Name of the bid winner and the bid amount will be displayed"]

def rules():
    for each_rule in rules_list:
        print(each_rule)
    choice = input(
        "Please choose an option:\n"
        " - Type `yes` to start the bidding process.\n"
        " - Type `no` to return to the main menu.\n"
        " - Type `rules` to view the rules again.\n"
        " - Type `exit` to close the program.\n"
        "Your choice: "
        )
    if choice.lower() == "yes":
        start_bidding()
    elif choice.lower() == "no":
        return
    elif choice.lower() == "rules":
        rules()
    elif choice.lower() == "exit":
        print("Exiting the program. Goodbye!")
        exit()

def start_bidding():
    global start, winner, bid_amount
    initial_bid_amount = 0
    print("The Bidding process is initiated" if(start == 'no') else "The Bid Battle 💰🔨 continues")
    print("Welcome to the Bid Battle! Let's get started!")
    has_initial_bid = random.choice([0,1])
    if (has_initial_bid and start == 'yet'):
        initial_bid_amount = random.randint(1, 1000)
        print(f"Initial bid is set to {initial_bid_amount}")
        start = 'yes'
    while (start !="no"):
        name = input("Enter your name: ")
        bid_amount = int(input("Enter your bid amount: $"))
        if (bid_amount <= 0):
            print("Invalid bid amount. Please enter a positive number.")
            continue
        if (bid_amount > initial_bid_amount if has_initial_bid else True):
            print(f"Your bid of ${bid_amount} is accepted")
            winner[len(winner)] = { name: bid_amount }
            # print(winner)
            if len(winner) == 1:
                pass_the_bid = 'yes'
                print("Bid is automatically passed to the next person to bid.")
            else:
                pass_the_bid = input("Do you want to pass the bid? (yes/no): ").strip()
                if pass_the_bid.lower() == "yes":   
                    print("Bid is passed to the next person.")
                elif pass_the_bid.lower() == "no":
                    print("Bid is not passed. Its time to declare the winner.")
                    start = 'no'
                    know_the_bid_winner()
        elif (bid_amount <= initial_bid_amount):
            print(f"Your bid of ${bid_amount} is lower than the initial bid. Please enter a bid higher than ${initial_bid_amount}.")
            continue

def know_the_bid_winner():
    global winner, start
    winner_index = 0
    winner_amount = 0
    winner_name = ''
    # print(winner)
    for each_winner_index in winner:
        for each_winner in winner.get(each_winner_index):
            if winner.get(each_winner_index).get(each_winner) > winner_amount:
                winner_index = each_winner_index
                winner_amount = winner.get(each_winner_index).get(each_winner)
                winner_name = each_winner
        # print(each_winner)

    print(f"The bid winner is {winner_name} with a bid amount of ${winner_amount} placed at {winner_index+1} turn. Congratulations")

process = [rules, start_bidding, know_the_bid_winner]

def welcome():
    print("Welcome to secret bidding system", "Here each person can stand a chance to win the jackpot bid","Bid today, Own forever", sep="\n")  

def menu_items():
    # print(process[0], str(process[0]))
    for each_process in process:
        # str_each_process = str(each_process)
        # print(str_each_process[str_each_process.index(' '):str_each_process.index('at')])

        # print(type(str_each_process) )
        # print(type(each_process.__name__))
        print(f"{process.index(each_process)+1}. {(each_process.__name__).capitalize()}")

menu = [welcome, menu_items]

def print_menu():
    for each_menu in menu:
        each_menu()

while(start != 'no'):
    print_menu()
    choice = int(input("Enter the choice"))
    if(choice in range(0, len(process))):
        process[choice-1]()
    