
def selection_sort(arr):
    # Looping through every element
    for i in range(len(arr)):

        # Searching the minimum element in subarry[i+1 to last element]
        min_index = i
        for j in range(i+1, len(arr)):

            if arr[j] < arr[min_index]:
                min_index = j
        # Swaping the minimum element and the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print("Sorted list:", my_list)

"""
Selection Sort is a simple sorting algorithm that sorts an array by repeatedly finding the minimum element
from the unsorted part of the array and putting it at the beginning.
The algorithm divides the array into a sorted and an unsorted region. In each iteration,
it finds the minimum element from the unsorted region and swaps it with the first element of the unsorted region

Selection Sort has a time complexity of O(n^2) and is not as efficient as more
 advanced sorting algorithms for large datasets.
However, it has the advantage of performing a minimal number of swaps.

"""