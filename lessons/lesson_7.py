# tuples
# to create a tuple with one element, add a comma e.g. (1,)
# isinstance() - to check if an item is a tuple, list etc
# we can delete a tuple but not its individual items

# dictionaries

'''
users = {}


while True:
    print("1. create user \n2. Delete user \n3. Print Users \n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        users[username] = password

    elif choice == "2":
        username = input("Enter username: ")
        if username in users:
            del users[username]
        else:
            print("User not found")
    elif choice == "3":
        for username, password in users.items():
            # dict_items([(username, password), (username, password)])
            print(f"Username: {username}, password: {password}")

    elif choice == "4":
        break
    else:
        print("Invalid choice")

        '''

D = dict() 
for x in enumerate(range(2)):
    D[x[0]] = x[1] 
    D[x[1]+7] = x[0] 
print(D)

# {0: 0, 7: 0, 1: 1, 8: 1}
# enumerate() will return a tuple, the loop will have x = (0, 0), (1, 1). Thus D[0] = 0, D[1] = 1, D[0 + 7] = D[7] = 0 and D[1 + 7] = D[8] = 1. Note: Dictionary is unordered, so the sequence of the key-value pair may differ in each output.