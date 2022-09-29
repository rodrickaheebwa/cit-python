# 8. Using list comprehension, write a program that takes a list of numbers and returns a list of the squares of the numbers.

def squares(arr):
    return [a**2 for a in arr]

print(squares([1,5,7,2]))