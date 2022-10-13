# Aheebwa Rodrick

# Number 1
print("----------------Number 1-------------------")
print("A program to sum all items in a list")
list_size = int(input("Enter the size of your list: "))
list_items = [ int(input("Enter item " + str(i+1) + " : " )) for i in range(list_size) ]
print("The sum of your items is " + str(sum(list_items)))

# Number 2
print("----------------Number 2-------------------")
sample_list = ['abc', 'xyz', 'aba', '1221', 'anbd', 'dbd']
string_counter = 0
for item in sample_list:
    if len(item) >= 2:
        if item[0] == item[-1]:
            string_counter += 1
print(string_counter)

# Number 3
print("----------------Number 3-------------------")
fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
new_list = []
for fruit in fruits:
    if fruit  not in new_list:
        new_list.append(fruit)
print(new_list)

# Number 4
print("----------------Number 4-------------------")
# sample_list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
print(sample_list)
del sample_list[0]
del sample_list[-2]
del sample_list[-1]
print(sample_list)

# Number 5
print("----------------Number 5-------------------")
print([i**2 for i in range(1,31) if i not in [1,2,3,4,5]])
