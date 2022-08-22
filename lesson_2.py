"""
1. input
2. calculate age program
3. conditionals
4. temperature convertor
"""

# input

#name = input("What is your name? ")
#colour = input("What is your favourite colour? ")
#print("Your name is " + name + " and your favourite colour is " + colour + ".")

# a simple program to calculate age

#current_year = 2022
#age = 0
#year_of_birth = int(input("In what year were you born? "))
#age = current_year - year_of_birth
#print("You are " + str(age) + " years old.")

# degrees celcius to fahreneit and vice versa from user

print("TEMPERATURE CONVERTOR")

conversion = int(input("Enter 1 to convert from celcius to fahrenheit or Enter 2 to convert from fahreneit to celcius: "))

if conversion == 1:
    celcius_degrees = int(input("Enter the temperature in celcius: "))
    fahrenheit_degrees = (celcius_degrees*(9/5)) + 32
    print(str(celcius_degrees) + " degrees celcius = " + str(fahrenheit_degrees) + " degrees fahrenheit")
elif conversion == 2:
    fahrenheit_degrees = int(input("Enter the temperature in fahrenheit: "))
    celcius_degrees = (5/9)*(fahrenheit_degrees-32)
    print(str(fahrenheit_degrees) + " degrees fahrenheit = " + str(celcius_degrees) + " degrees celcius")
else:
    print("Invalid input.")