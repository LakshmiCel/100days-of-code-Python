total = 0 

def add(var1, var2):
    # print("add called")
    return var1 + var2

 
def subtract(var1, var2):
    return var1 - var2

 
def multiply(var1, var2):
    return var1 * var2

 
def exponent(var1, var2):
    return var1 ** var2
 
def divide(var1, var2):
    return var1 / var2
 
def mod(var1, var2):
    return var1 % var2


operations_dict = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '**' : exponent,
    '/' : divide,
    '%' : mod
}
# operations_dict['+']()

def first_number_call():
    if total:
        print(f"First number {total} will be from the previous result")
        return total
    elif total == 0:
        return int(input("Enter the number in the first position: ").strip())

def operator_call():
    operator = input("Enter the operator you want to use: ").strip()
    if(operator not in operations_dict.keys()):
        print("Invalid operator. Please try again.")
        return operator_call()
    return operator

def continuation():
    can_continue = input("Enter `yes` to continue or `no` to exit: ").strip()
    if(can_continue in ('yes','no')):
        return can_continue
    else:
        print("Invalid input. Please try enterring yes or no")
        return continuation()

start = 'yes' 
while start == 'yes':
    print("Welcome to the calculator app", end = "\n\n")
    first_number = first_number_call()
    print("You have entered: ", first_number, end = "\n")
    print(f"Operators list: {list(operations_dict.keys())} ")
    operator = operator_call()
    second_number = int(input("Enter the number in the second position: ").strip())
    print("You have entered: ", second_number, end = "\n")
    result = operations_dict[operator](first_number, second_number)
    print(f" Result : {first_number} {operator} {second_number} = {result}")
    can_continue = continuation()
    if (can_continue == 'yes'):
        total = result
    else :
        start = can_continue
        total = 0