# Day 10 of 100 Days of Code
# Calculator with addition, subtraction, multiplication, and division

from art import logo

print(logo)


def clear():
    return "\x1B[2J"


# Addition
def addition(a, b):
    return a + b


# Subtraction
def subtraction(a, b):
    return a - b


# Multiplication
def multiplication(a, b):
    return a * b


# Division
def division(a, b):
    return a / b


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}


def operation_decider():
    decision = input("Pick an operation: ")
    for key in operations:
        if decision == key:
            final_op = operations[key]
    return final_op, decision


def rounding(number):   # If the number is whole, return as an integer for prettiness
    if number % 1 == 0:
        return int(number)
    else:
        return number


def calculator():
    print(f"Available operations: ")
    for key in operations:
        print(key)
    num1 = float(input("What's the first number?: "))

    continuing = True

    while continuing:
        function, fun_str = operation_decider()     # Decide on / * + -
        num2 = float(input("What's the next number?: "))
        answer = function(num1, num2)               # function name is / * + -
        print(f"{num1} {fun_str} {num2} = {rounding(answer)}")
        should_continue = input(f"Would you like to perform another operation "
                                f"with {rounding(answer)}? Yes or No: ").lower()
        if not should_continue == "yes":
            continuing = False
            print(clear())
            print(logo)
            calculator()
        else:
            num1 = answer  # resetting answer for the while loop


calculator()
