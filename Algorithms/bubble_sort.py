def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    #The outer loop (for i in range(n)) iterates through each element in the array.
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        # The inner loop (for j in range(0, n-i-1)) compares adjacent elements and swaps them if they are in the wrong order.
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


listanumere = [32, 7, 65, 2, 89, 3, 95]
bubble_sort(listanumere)
print(listanumere)


def bubble_sort_string(yourstring):
    stringlist = list(yourstring)
    n = len(stringlist)

    for i in range(n):
        for j in range(0, n - i - 1):
            if stringlist[j] > stringlist[j + 1]:
                stringlist[j], stringlist[j + 1] = stringlist[j + 1], stringlist[j]
    sortedstring = ''.join(stringlist)
    return sortedstring


yourstring = 'stronger'
print(bubble_sort_string(yourstring))

"""
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements, and swaps them if they are in the wrong order.
---
Bubble Sort is not the most efficient sorting algorithm, especially for large datasets, 
but it is easy to understand and implement.
"""