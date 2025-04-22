from datetime import datetime, date
pizza_variety = {
    'Personal': 250,
    'Classic': 399,
    'Grande': 499,
    'Venti': 599
}

toppings = {
    'Pepperoni': 50,
    'Sausage': 50,
    'Mushrooms': 50,
    'Onions': 50,
    'Bell Peppers': 50,
    'Extra Cheese': 100,
    'Paneer': 75,
}
current_cart_item_index = "1"
cart = {
}

# print(cart[current_cart_item_index])
pizza_items = list(pizza_variety.items())
topping_items = list(toppings.items())

def place_order():
    # while True:
    #     order_pizza(current_cart_item_index)
    #     order_toppings(current_cart_item_index)
    #     for order in cart:
    #         pizza_list = list(cart[order]["size"])
    #         toppings_list = list(cart[order]["toppings"])
    #         # print(cart[current_cart_item_index])
    #         print("Order placed for " +  " , ".join( (str(cart[order]["size"][i]) + " " + str(i)) if cart[order]["size"][i] > 1 else str(i) for i in pizza_list)+ (" pizza" if len(pizza_list) == 1 else " pizzas") , end=" ")
    #         print(" with "+ " , ".join((str(cart[order]["toppings"][i]) + " " + str(i)) if cart[order]["toppings"][i] > 1 else str(i)  for i in toppings_list) + (" topping" if (len(toppings_list) == 1 and cart[order]["toppings"][toppings_list[-1]] == 1) else " toppings"))
    #     break
    while True:
        global current_cart_item_index
        order_pizza(current_cart_item_index)
        order_toppings(current_cart_item_index)

        another_pizza_statement = "Do you want another pizza with toppings? Enter y or n: "
        another_pizza = input(another_pizza_statement).strip().lower()

        if another_pizza == "y":
            cart_item_index = str(int(current_cart_item_index) + 1)
            current_cart_item_index = cart_item_index
        elif another_pizza == "n":
            for order in cart:
                pizza_list = list(cart[order]["size"])
                toppings_list = list(cart[order]["toppings"])
                print("Order placed for " + " , ".join(
                        (str(cart[order]["size"][i]) + " " + str(i)) if cart[order]["size"][i] > 1 else str(i)
                        for i in pizza_list) +
                        (" pizza" if len(pizza_list) == 1 else " pizzas"), end=" ")

                print("with " + " , ".join(
                        (str(cart[order]["toppings"][i]) + " " + str(i)) if cart[order]["toppings"][i] > 1 else str(i)
                        for i in toppings_list) +
                        (" topping" if (len(toppings_list) == 1 and cart[order]["toppings"][toppings_list[-1]] == 1) else " toppings"))

            run_from_start()
            return
            # break
        else:
            print("Invalid choice. Back to menu.")
            # main_menu()
            run_from_start()
            return
            # break

def order_pizza(cart_item_index):
    print("Please select your pizza size:", end="\n\n")
    variety_index = []
    for i, variety in enumerate(pizza_variety):
        variety_index.append(i+1);
        print(f" {i+1} {variety}: ${pizza_variety[variety]}")
    # print(variety_index)
    choice_print_statement = "Enter the choice from "+"/".join(str(variety) for variety in variety_index) +  " "*4   
    choice_pizza_variety = int(input(choice_print_statement))
    # print(int(choice_pizza_variety) in variety_index)
    if(choice_pizza_variety not in variety_index):
        print("\nInvalid choice, Please " + choice_print_statement)
        order_pizza(cart_item_index)
    # print(variety_index, pizza_items[int(choice_pizza_variety)-1])
    elif (choice_pizza_variety in variety_index):
        cart[cart_item_index] = {"size": {}, "toppings":{}, "price":{}}
        # print(cart)
        pizza, prize = pizza_items[choice_pizza_variety-1]
        # print(pizza, prize, 'pp')
        cart[cart_item_index]["size"][pizza] = (1 if(pizza not in cart[cart_item_index]["size"]) else (cart[cart_item_index]["size"][pizza] + 1))
        cart[cart_item_index]["price"] = prize
    # print(cart["pizza"])
    # print(cart[cart_item_index]["size"][pizza], 'cart pizza')

def order_toppings(cart_item_index):
    # global cart_item_index
    # print(cart_item_index, 'ccindex')
    print("Please select your toppings for "+ list(cart[cart_item_index]["size"])[0] +" size pizza" ,end="\n\n")
    variety_index = []
    for i, variety in enumerate(toppings):
        variety_index.append(i+1);
        print(f" {i+1} {variety}: ${toppings[variety]}")
    # print(variety_index)
    choice_print_statement = "Enter the choice from "+"/".join(str(variety) for variety in variety_index) +  " "*4   
    choice_topping_variety = input(choice_print_statement)
    # print(int(choice_topping_variety) in variety_index)
    if(int(choice_topping_variety) not in variety_index):
        print("\nInvalid choice, Please " + choice_print_statement)
        return order_toppings(cart_item_index)
    # print(variety_index, pizza_items[int(choice_pizza_variety)-1])
    topping, prize = topping_items[int(choice_topping_variety)-1]
    cart[cart_item_index]["price"] += prize
    cart[cart_item_index]["toppings"][topping] = (1 if(topping not in cart[cart_item_index]["toppings"]) else (cart[cart_item_index]["toppings"][topping] + 1))
    another_topping_statement = "Do you want another topping. Enter y or n\n"
    another_topping = input(another_topping_statement).strip().lower()
    if(another_topping == "y"):
        order_toppings(cart_item_index)
    elif(another_topping not in ("y", "n")):
        print("Invalid choice")
        order_toppings(cart_item_index)
    return

sub_total= 0
def view_cart(should_checkout):
    global sub_total
    # print("Viewing Cart...")
    print("\n✨ Your Pizza Cart at La Pizzaría – MG Road, Bengaluru ✨")
    print("="*70)
    print("La Pizzaria" , "Invoice", sep=" "*40)
    print("Invoice : "+ str(datetime.now()) + " "*15 + "Date: " + str(date.today()))
    print("="*70)
    for item in cart:
        pizza_list = list(cart[item]["size"])
        toppings_list = list(cart[item]["toppings"])
        # print(str(cart[item]["size"])+"------"+str(cart[item]["price"]))
        print(" , ".join(
                (str(cart[item]["size"][i]) + " " + str(i)) if cart[item]["size"][i] > 1 else str(i) for i in pizza_list) +
                (" pizza" if len(pizza_list) == 1 else " pizzas"), end=" ")

        print("with " + " , ".join(
                (str(cart[item]["toppings"][i]) + " " + str(i)) if cart[item]["toppings"][i] > 1 else str(i) for i in toppings_list) +
                (" topping" if (len(toppings_list) == 1 and cart[item]["toppings"][toppings_list[-1]] == 1) else " toppings"), end=" ")
        sub_total = (cart[item]["price"] + sub_total) if(not should_checkout) else sub_total
        print("-"*10 + str(cart[item]["price"]))
    print("\nCart is empty\n" if(sub_total == 0) else ("\nSubtotal:  " + str(sub_total)), end="\n")
    print("="*70, end="\n\n")
    cgst = (sub_total*2.5)/100
    print("CGST @2.5%: " + str(cgst))
    print("SGST @2.5%: " + str(cgst), end="\n\n")
    print("="*70)
    print("\nTotal: " + str(sub_total + cgst + cgst), end="\n\n")
    print("="*70)
    if(not should_checkout):
        run_from_start()
    
def apply_promo():
    print("Applying Promo Code...")

def discounted_price(promo, discount):
    print("Promo " + promo + " applied!")
    cgst = (sub_total*2.5)/100
    # print("CGST @2.5%: " + str(cgst))
    print("Disount: " + str(-((sub_total*discount)/100)), end="\n\n")
    print("-"*70)
    print("\nTotal: " + str(sub_total + cgst + cgst - ((sub_total*discount)/100)), end="\n\n")
    print("-"*70)

def checkout():
    global cart, sub_total
    view_cart(True)
    if(len(cart)):
        promo = input("Enter the promo code. If you have any")
        if promo == "LAPIZZA10":
            print("10% off on your order")
            discounted_price(promo, 10)
        if promo.endswith('5'):
            print("5% off on your order")
            discounted_price(promo, 5)

        print("Thank you for ordering at La Pizzaría – MG Road, Bengaluru. Visit us again")
        cart={}
        sub_total=0
        run_from_start()
    elif len(cart)==0:
        print("\nCart is empty. Please add items to cart to proceed to checkout\n\n")
    run_from_start()
    # print("Proceeding to Checkout...")

def exit_system():
    print("Thank you for visiting La Pizzaría!")
    exit()

def main_menu():
    print("Main Menu:")
    print("1. Place an Order")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

menu_actions = {
    "1": place_order,
    "2": view_cart,
    "3": checkout,
    "4": exit_system,
}

def welcome_message():
    print("═"*55)
    print("🍕  Welcome to La Pizzaría – MG Road, Bengaluru  🍕")
    print("═"*55)
    print("Taste deliciousness with every slice of pizza", end="\n\n")

def run_menu():
    choice = input("Please enter your choice: ")
    action = menu_actions.get(choice)
    
    if action:
        action(False) if action == view_cart else action()
    else:
        print("Invalid choice, please try again.")
        # welcome_message()
        # main_menu()
        # run_menu()
        run_from_start()

def run_from_start():
    welcome_message()
    main_menu()
    run_menu()
# welcome_message()
# main_menu()
# run_menu()

run_from_start()
# while True:
