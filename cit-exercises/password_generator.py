# python program that generates a random password for a user
# user enters length they want; not less than 6
# how many letters and numbers they want
# password should be a mix of uppercase, lowercase, symbols, numbers

import string, random

password = []

while True:
    length = int(input("Enter how many characters you want in your password (not less than 6): "))
    if length >= 6:
        letters_length = int(input("How many letters do you want in your password?: "))
        if letters_length <= length:
            numbers_length = int(input("How many numbers do you want in your password?: "))
            if numbers_length <= length and numbers_length + letters_length <= length:
                symbols_length = length - (numbers_length + letters_length)
                break
            else:
                print("Your requirements exceed password length")
        else:
            print("You want more letters than the password length")
    else:
        print("Length entered is less than 6")

for i in range(letters_length):
    password.append(random.choice(string.ascii_letters))

for i in range(numbers_length):
    password.append(str(random.randint(0,9)))

for i in range(symbols_length):
    password.append(random.choice([':', '+', '@', '^', '%', '(', '-', '*', '|', '&', '<', '_', '=', '!', '>', '?', '#', '$', ')']))

random.shuffle(password)
print("Your password is: ", ''.join(password))