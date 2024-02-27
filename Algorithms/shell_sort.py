
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        gap //= 2

my_list = [64, 25, 12, 22, 11]
shell_sort(my_list)
print("Sorted list:", my_list)

"""
Shell Sort is an in-place comparison sort algorithm that is an extension of the insertion sort. 
It works by sorting subarrays with a specific gap size and gradually reducing the gap until the entire array is sorted. 

"""