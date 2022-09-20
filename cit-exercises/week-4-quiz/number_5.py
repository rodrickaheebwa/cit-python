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

# Iden solution
def fetch_email(file: str) -> list:
    """Fetches the email from a text file
    Args:
        file (str): The text file
    Returns:
        list: The emails
    """
    import re

    emails = []
    with open(file, "r") as f:
        for line in f:
            emails.append(re.search(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", line).group())