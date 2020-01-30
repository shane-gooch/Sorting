# STRETCH: implement Linear Search
def linear_search(arr, target):

  # TO-DO: add missing code
    for i in range(0, len(arr)):
        if target == arr[i]:
            return i
    else:
        return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
  # Cut arr in half
  # Compare target to middle value
  # Depending on which side is bigger, move to that side

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    while low <= high:
        middle = (low + high) / 2
        if arr[middle] < target:
            low = middle + 1
        elif arr[middle] > target:
            high = middle - 1

    # TO-DO: add missing code

    return -1  # not found


# arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
# test = linear_search(arr1, 7)
# print(test)

# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
