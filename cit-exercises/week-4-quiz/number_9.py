# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

import sys

if len(sys.argv) == 2:
    my_list = sys.argv[1].split(',')
    print(my_list)
    print(tuple(my_list))
else:
    print("Pass a comma separated list of numbers as a commandline argument")