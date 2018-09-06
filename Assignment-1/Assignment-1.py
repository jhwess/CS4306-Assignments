# Course:        CS4306
# Student name:  Jackson Wessels
# Student ID:    000-50-9463
# Assignment #:  #1
# Due Date:      09/06/2018
# Signature:     JHW
# Score:
from random import randrange


def binary_search(array, left, right, target):
    # If our target value is found within the portion of the array, we will insert at that index.
    # If the target is not found, we will insert at the current middle position after the search has completed.
    target_found = False
    middle = None
    while left <= right and not target_found:
        middle = (left + right) // 2
        if array[middle] == target:
            target_found = True
        else:
            if target < array[middle]:
                right = middle - 1
            else:
                left = middle + 1

    return middle


def insertion_sort(array):
    for i in range(1, len(array)):
        # Value to be inserted
        insert_val = array[i]
        # Determine insertion index using binary search
        insert_index = binary_search(array, 0, i - 1, insert_val)
        # Perform an additional comparison to make sure our insertion value is not greater than the value at
        # the insertion point.
        if insert_val > array[insert_index]:
            insert_index += 1
        # Perform insertion of value and shift array
        array = array[:insert_index] + [insert_val] + array[insert_index:i] + array[i + 1:]

    return array


unsorted_array = []
for idx in range(0, 49):
    unsorted_array.append(randrange(50))

sorted_array = insertion_sort(unsorted_array)
print("Unsorted array:")
print(str(unsorted_array) + "\n")
print("Sorted array using binary insertion sorting algorithm:")
print(sorted_array)
