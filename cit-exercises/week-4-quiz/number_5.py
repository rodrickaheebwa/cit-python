# Write a python program to fetch only Email ID from text file which include following fields -:
# Name
# Mobile Number
# Roll Number
# Email ID

try:
    ex_file = open("example_file.txt", "r")

    lines = ex_file.readlines()
    for line in lines:
        if line.strip() == 'Email ID':
            print(line.strip())
except:
    print("An error occurred")
finally:
    ex_file.close()