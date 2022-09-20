# Binary Search
def binary_search(numbers: list, number: int) -> int:
    """Searches for a number in a list using binary search
    Args:
        numbers (list): The numbers
        number (int): The number to search for
    Returns:
        int: The index of the number
    """
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == number:
            return mid
        elif numbers[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))