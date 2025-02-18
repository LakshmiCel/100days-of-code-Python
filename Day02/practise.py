print("Welcome to the bill tip calculator")
print("Enter the total amount of the bill")
amount=float(input())
print("Enter the tip percent you would like to give like 10, 12 or 20")
percent= float(input())/100
print("Enter the persons between which we need to split the bills")
persons=int(input())
tip_amount=0
if(percent!=0):
    tip_amount=amount*percent
print("The mount to be paid by single person", (amount + tip_amount) / persons)