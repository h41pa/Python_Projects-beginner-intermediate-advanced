def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
my_list = [64, 25, 12, 22, 11]
merge_sort(my_list)
print("Sorted list:", my_list)

"""
Merge Sort is a divide-and-conquer algorithm that works by recursively 
breaking down the input array into smaller subarrays, sorting them, and then merging them back together. 
The core idea is to divide the array into two halves, sort each half, 
and then merge them in a way that ensures the merged array is sorted.

---
The merge_sort function takes an array arr as a parameter.
If the length of the array is greater than 1, it is divided into two halves (left_half and right_half).
The function is called recursively to sort each half separately.
The sorted halves are then merged back together.

Merge Sort has a time complexity of O(n log n) and is a stable sorting algorithm. 
It is efficient for large datasets but may require additional space for the merging process.

"""





