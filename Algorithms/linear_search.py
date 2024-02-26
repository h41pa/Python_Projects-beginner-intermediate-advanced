def linear_search(arr, target):
    n = len(arr)
    for index in range(n):
        if arr[index] == target:
            return index

    return -1


my_list = [4, 2, 7, 1, 9, 5]
search_target = 9
print(linear_search(my_list, search_target))


def linear_search_enumerate(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index

    return -1

"""
 Linear Search is a simple search algorithm that 
 sequentially checks each element in a list until a match is found or the entire list has been searched.
 
 Linear Search is straightforward but may not be as efficient as other search algorithms for large datasets.
"""