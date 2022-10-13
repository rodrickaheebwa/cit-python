# Write a function that takes a list of numbers and returns the largest number in the list

def max(arr):
    m = arr[0]
    for elem in arr:
        if elem > m:
            m = elem
    return m

print(max([1,8,1,5]))