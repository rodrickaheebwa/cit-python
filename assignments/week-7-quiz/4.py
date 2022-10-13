# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

import string

def case_count(str):
    upp = 0
    low = 0
    for letter in str:
        if letter in string.ascii_lowercase:
            low += 1
        if letter in string.ascii_uppercase:
            upp += 1
    return f"UPPER CASE {upp} LOWER CASE {low}"
    

print(case_count("HW"))