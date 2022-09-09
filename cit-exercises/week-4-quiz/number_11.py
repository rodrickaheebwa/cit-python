# Write a function to compute 5/0 and use try/except to catch the exceptions.

def zero_try_except():
    try:
        print(5/0)
    except ZeroDivisionError as error:
        print(f"An error occurred: {error}")

zero_try_except()