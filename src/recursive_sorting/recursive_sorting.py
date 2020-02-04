# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    merged_arr = []
    a, b = 0, 0
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1
    if a == len(arrA):
        merged_arr.extend(arrB[b:])
    else:
        merged_arr.extend(arrA[a:])
    return merged_arr


a = [1, 23, 4]
b = [5, 8, 3]
print('sorted', merge(a, b))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # break list in half until len(list) == 1
    if len(arr) <= 1:
        return arr
    else:
        lhs = merge_sort(arr[:len(arr) // 2])
        rhs = merge_sort(arr[len(arr)//2:])
    return merge(lhs, rhs)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


arr1 = [1, 5, 8, 4, 2, -9, 64, 0, 3, 7]
print(merge_sort(arr1))
