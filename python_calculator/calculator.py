# Python Calculator

operator = input("Enter an operator (+ - * /): ") # Prompts user to select an arithmetic operator
num1 = float(input("Enter the first number: ")) # Prompts user to input a value for num1
num2 = float(input("Enter the second number: ")) # Prompts user to input a value for num2

if operator == "+":
    result = num1 + num2 # value of num1 and num2 are added if user chooses "+"
    print(round(result, 2)) # prints out result
elif operator == "-":
    result = num1 + num2 # value of num1 and num2 are subtracted if user chooses "-"
    print(round(result, 2)) # prints out result
elif operator == "*":
    result = num1 * num2 # value of num1 and num2 are multiplied if user chooses "*"
    print(round(result, 2)) # prints out result
elif operator == "/":
    result = num1 / num2 # value of num1 and num2 are divided if user chooses "/"
    print(round(result, 2)) # prints out result

else:
    print(f"{operator} is not a valid operator.") # lets user know chosen operator is invalid
    