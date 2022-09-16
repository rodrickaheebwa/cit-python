# cli to add, subtract, multiply, divide two numbers in terminal

import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="Terminal Calculator")
    parser.add_argument('-a', '--add', help='Add numbers')
    parser.add_argument('-s', '--subtract', help='Subtract numbers')
    parser.add_argument('-m', '--multiply', help='Multiply numbers')
    parser.add_argument('-d', '--divide', help='Divide numbers')
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.add:
        try:
            num1, num2 = tuple(args.add.split(','))
            print(int(num1) + int(num2))
        except:
            print("invalid input")
    elif args.subtract:
        try:
            num1, num2 = tuple(args.subtract.split(','))
            print(int(num1) - int(num2))
        except:
            print("invalid input")
    elif args.multiply:
        try:
            num1, num2 = tuple(args.multiply.split(','))
            print(int(num1) * int(num2))
        except:
            print("invalid input")
    elif args.divide:
        try:
            num1, num2 = tuple(args.divide.split(','))
            print(int(num1) / int(num2))
        except:
            print("invalid input")
    else:
        parser.print_help()

main()