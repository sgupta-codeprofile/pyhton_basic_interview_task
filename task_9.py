# Task 9

# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

def binary_search(alist, key):
    start = 0
    end = len(alist)
    while start < end:
        mid = (start + end)//2
        if alist[mid] > key:
            end = mid
        elif alist[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1

alist = [2, 3, 4, 10, 40]
key = 10

index = binary_search(alist, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))