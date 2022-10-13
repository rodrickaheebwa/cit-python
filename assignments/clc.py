# command line calculator

import sys

def add(num1, num2):
    print(num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)

def multiply(num1, num2):
    print(num1 * num2)

def divide(num1, num2):
    print(num1/num2)

def usage():
    '''
    How to use the command line calculator.
    '''
    print("-----------------------------")
    print("Simple command line calculator")
    print("Performs operations of addition, subtraction, multiplication and division on TWO numbers")
    print("Usage: clc.py <add/subtract/multiply/divide> <number1> <number2>")
    print("-----------------------------")

def calculator():
    if len(sys.argv) == 4:
        operator = sys.argv[1]
        num1 = int(sys.argv[2])
        num2 = int(sys.argv[3])
        if operator == 'add':
            add(num1, num2)
        elif operator == 'subtract':
            subtract(num1, num2)
        elif operator == 'multiply':
            multiply(num1, num2)
        elif operator == 'divide':
            divide(num1, num2)
        else:
            print("Invalid operation")

    else:
        usage()
        sys.exit(-1)

def main():
    calculator()


if __name__ == '__main__':
    main()