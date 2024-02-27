
def insertion_sort(arr):
    # Traversing through 1 to the length of the array
    for i in range(1,len(arr)):
        key = arr[i]


        # Moving elements of array[0..i-1], that are
        # bigger than the key, to one index ahead
        # of their current index
        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    
my_list = [64, 25, 12, 22, 11]
insertion_sort(my_list)
print("Sorted list:", my_list)

"""
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time.
It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
However, it performs well for small lists or lists that are almost sorted.

Insertion Sort has a time complexity of O(n^2) in the worst case, but its simplicity and 
efficiency on small datasets make it a reasonable choice in certain scenarios.

"""