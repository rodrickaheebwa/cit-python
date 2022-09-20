# Algorithm challenge: Create your own sorting algorithm.

# merge sort
def split_list(numbers: list) -> tuple:
    """Splits a list into two
    Args:
        numbers (list): The numbers
    Returns:
        tuple: The two lists
    """
    half = len(numbers) // 2
    
    return numbers[:half], numbers[half:]

def merge_lists(list1: list, list2: list) -> list:
    """Merges two lists
    Args:
        list1 (list): The first list
        list2 (list): The second list
    Returns:
        list: The merged list
    """
    merged_list = []
    while list1 and list2:
        if list1[0] < list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))
    merged_list.extend(list1)
    merged_list.extend(list2)
    return merged_list

def merge_sort(numbers: list) -> list:
    """Sorts a list using merge sort
    Args:
        numbers (list): The numbers
    Returns:
        list: The sorted list
    """
    if len(numbers) <= 1:
        return numbers
    list1, list2 = split_list(numbers)
    list1 = merge_sort(list1)
    list2 = merge_sort(list2)
    return merge_lists(list1, list2)

print(merge_sort([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][::-1]))

# Bubble Sort
def bubble_sort(numbers: list) -> list:
    """Sorts a list using bubble sort
    Args:
        numbers (list): The numbers
    Returns:
        list: The sorted list
    """
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

print(bubble_sort([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][::-1]))

# Insertion Sort
def insertion_sort(numbers: list) -> list:
    """Sorts a list using insertion sort
    Args:
        numbers (list): The numbers
    Returns:
        list: The sorted list
    """
    for i in range(1, len(numbers)):
        j = i - 1
        key = numbers[i]
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

print(insertion_sort([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][::-1]))

# Selection Sort
def selection_sort(numbers: list) -> list:
    """Sorts a list using selection sort
    Args:
        numbers (list): The numbers
    Returns:
        list: The sorted list
    """
    for i in range(len(numbers) - 1):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

print(selection_sort([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][::-1]))

# Quick Sort
def quick_sort(numbers: list) -> list:
    """Sorts a list using quick sort
    Args:
        numbers (list): The numbers
    Returns:
        list: The sorted list
    """
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    left = [number for number in numbers[1:] if number < pivot]
    right = [number for number in numbers[1:] if number >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][::-1]))

# Heap Sort
def heapify(numbers: list, n: int, i: int) -> None:
    """Heapifies a list
    Args:
        numbers (list): The numbers
        n (int): The length of the list
        i (int): The index
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and numbers[i] < numbers[left]:
        largest = left
    if right < n and numbers[largest] < numbers[right]:
        largest = right
    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]
        heapify(numbers, n, largest)

def heap_sort(numbers: list) -> list:
    """Sorts a list using heap sort
    Args:
        numbers (list): The numbers
    Returns:
        list: The sorted list
    """
    n = len(numbers)
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, n, i)
    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)
    return numbers

print(heap_sort([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][::-1]))

# Counting Sort
def counting_sort(numbers: list) -> list:
    """Sorts a list using counting sort
    Args:
        numbers (list): The numbers
    Returns:
        list: The sorted list
    """
    max_number = max(numbers)
    count = [0] * (max_number + 1)
    for number in numbers:
        count[number] += 1
    i = 0
    for number in range(max_number + 1):
        for j in range(count[number]):
            numbers[i] = number
            i += 1
    return numbers

# Radix Sort
def counting_sort_radix(numbers: list, exp: int) -> list:
    """Sorts a list using counting sort(for radix sort)
    Args:
        numbers (list): The numbers
        exp (int): The exponent
    Returns:
        list: The sorted list
    """
    n = len(numbers)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = numbers[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = numbers[i] // exp
        output[count[index % 10] - 1] = numbers[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        numbers[i] = output[i]
    return numbers

def radix_sort(numbers: list) -> list:
    """Sorts a list using radix sort
    Args:
        numbers (list): The numbers
    Returns:
        list: The sorted list
    """
    max_number = max(numbers)
    exp = 1
    while max_number // exp > 0:
        counting_sort_radix(numbers, exp)
        exp *= 10
    return numbers

# Bucket Sort
def bucket_sort(numbers: list) -> list:
    """Sorts a list using bucket sort
    Args:
        numbers (list): The numbers
    Returns:
        list: The sorted list
    """
    max_number = max(numbers)
    size = max_number // len(numbers)
    buckets = [[] for _ in range(len(numbers) + 1)]
    for number in numbers:
        i = min(number // size, len(numbers))
        buckets[i].append(number)
    numbers = []
    for bucket in buckets:
        insertion_sort(bucket)
        numbers.extend(bucket)
    return numbers

# Shell Sort
def shell_sort(numbers: list) -> list:
    """Sorts a list using shell sort
    Args:
        numbers (list): The numbers
    Returns:
        list: The sorted list
    """
    n = len(numbers)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j -= gap
            numbers[j] = temp
        gap //= 2
    return numbers

# Comb Sort
def comb_sort(numbers: list) -> list:
    """Sorts a list using comb sort
    Args:
        numbers (list): The numbers
    Returns:
        list: The sorted list
    """
    gap = len(numbers)
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(numbers):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                sorted = False
            i += 1
    return numbers

# Cycle Sort
def cycle_sort(numbers: list) -> list:
    """Sorts a list using cycle sort
    Args:
        numbers (list): The numbers
    Returns:
        list: The sorted list
    """
    writes = 0
    for cycle_start in range(len(numbers) - 1):
        item = numbers[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, len(numbers)):
            if numbers[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == numbers[pos]:
            pos += 1
        numbers[pos], item = item, numbers[pos]
        writes += 1
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(numbers)):
                if numbers[i] < item:
                    pos += 1
            while item == numbers[pos]:
                pos += 1
            numbers[pos], item = item, numbers[pos]
            writes += 1
    return numbers

# Linear search
def linear_search(numbers: list, number: int) -> int:
    """Searches for a number in a list using linear search
    Args:
        numbers (list): The numbers
        number (int): The number to search for
    Returns:
        int: The index of the number
    """
    for i in range(len(numbers)):
        if numbers[i] == number:
            return i
    return -1
