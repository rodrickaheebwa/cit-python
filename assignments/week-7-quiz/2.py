# The snail climbs up 7 feet each day and slips back 2 feet each night. How many days will it take the snail to get out of a well with the given depth?. Using python, write a function to solve this problem. Sample Input: 31 Sample Output: 6

def days_taken(depth):
    days = 0
    while depth > 0:
        days += 1
        depth -= 7
        if depth <= 0:
            break
        depth += 2
    return days

print(days_taken(31))