# 10. Using a while loop, implement merge sort algorithm

def mergesort(arr):
    if len(arr) < 2:
        return arr
     
    result = []
    mid = int(len(arr) / 2)  
     
    y = mergesort(arr[:mid])
    z = mergesort(arr[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result

print(mergesort([5,8,1,2,4,7,6,0,5]))