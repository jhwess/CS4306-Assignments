# Course:        CS4306
# Student name:  Jackson Wessels
# Student ID:    000-50-9463
# Assignment #:  #1
# Due Date:      09/06/2018
# Signature:     JHW
# Score:
from math import trunc
from random import randrange


def binary_search(array, right, left, target):
    # binary search here
    print("binary search")
    left = 0
    while left <= right:
        middle = trunc((left + right) / 2)
        if array[middle] < target:
            left = middle + 1
        elif array[middle] > target:
            right = middle - 1
        else:
            return middle


def insertion_sort(array):
    # insertion sort
    print("insertion sort")
    for i in range(1, len(array)):
        to_insert = binary_search(array, i, array[i])
        swap_value = array[i]
        j = i - 1
        while j >= to_insert:
            array[j + 1] = array[j]
            j -= 1
        array[to_insert] = swap_value

    return array


unsorted_array = []
for i in range(0, 19):
    unsorted_array.append(randrange(50))

sorted_array = insertion_sort(unsorted_array)
print("Unsorted array:")
print(str(unsorted_array) + "\n")
print("Sorted array using binary insertion sorting algorithm:")
print(sorted_array)
