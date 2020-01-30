# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i
        for x in range(current_index + 1, len(arr)):
            current_min = arr[current_index]

            if arr[x] < current_min:
                current_min = arr[x]
                temp = arr[i]
                arr[i] = current_min
                arr[x] = temp

        # TO-DO: find next smallest element

        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


test_selection = selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# print(test_selection)
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    for i in range(0, len(arr) - 1):
        for x in range(i + 1, len(arr)):
            if arr[x] < arr[i]:
                temp = arr[i]
                arr[i] = arr[x]
                arr[x] = temp

    return arr


test_bubble = bubble_sort([1, 5, 8, 400, 2, 9, 6, 0, 3, 7])
print(test_bubble)
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
