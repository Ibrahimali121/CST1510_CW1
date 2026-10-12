#Calculator
#Uses: functions, parameters, return, calling one function from another
#Define a function add(n1, n2) that returns n1 + n2.
#Define a function subtract(n1, n2) that returns n1 - n2.
#Define a function multiply(n1, n2) that returns n1 * n2.
#Define a function divide(n1, n2) that returns n1 / n2.
#Use input() to ask for the first number. Convert it with float() and store it in n1.
#Create a variable keep_going and set it to True.
#Start a while keep_going: loop.
#Inside the loop, ask for an operator (+ - * /) and store it in operator.
#Ask for the second number, convert it with float(), and store it in n2.
#Use if/elif to call the matching function and store the answer in result. For example, if operator == "+", then result = add(n1, n2).
#Print the calculation and the result.
#Ask the user: "Type 'y' to continue with the result, or 'n' to start over:"
#If they type "y", set n1 = result.
#O#therwise, ask for a new first number and store it in n1.
#E nxtension, once you've done Week 4: replace the if/elif in step 10 with a dictionary: operations = {"+": add, "-": subtract, "*": multiply, "/": divide} Then call result = operations[operator](n1, n2)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


print(add(2, 3))
print(subtract(5, 2))
print(multiply(3, 4))
print(divide(10, 2))   

N1 = float(input("Enter the first number: "))
keep_going = True
while keep_going:
    operator = input("Enter an operator (+, -, *, /): ")
    N2 = float(input("Enter the second number: "))
    
    if operator == "+":
        result = add(N1, N2)
    elif operator == "-":
        result = subtract(N1, N2)
    elif operator == "*":
        result = multiply(N1, N2)
    elif operator == "/":
        result = divide(N1, N2)
    else:
        print("Invalid operator. Please try again.")
        continue
    
    print(f"{N1} {operator} {N2} = {result}")
    
    continue_choice = input("Type 'y' to continue with the result, or 'n' to start over: ")
    if continue_choice.lower() == 'y':
        N1 = result
    else:
        N1 = float(input("Enter the first number: "))
