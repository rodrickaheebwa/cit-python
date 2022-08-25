# tuples
# to create a tuple with one element, add a comma e.g. (1,)
# isinstance() - to check if an item is a tuple, list etc
# we can delete a tuple but not its individual items

# dictionaries


users = {}

# {"iden": "1234", "bob": "345"}


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