# 3. Write a python program to find the maximum and minimum value in a given 2-D array

my_array = [[5,0,3,11], [2,14,3,6], [7,-2,9,11], [8, 2,10,3]]

max_number = max(max(inner_list) for inner_list in my_array)

min_number = min(min(inner_list) for inner_list in my_array)

print(f"Maximum number is {max_number} and Minimum number is {min_number}")