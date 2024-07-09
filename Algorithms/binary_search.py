
def binary_search(arr, target):
    left, right = 0, len(arr) -1

    while left <= right:
        mid = (left + right) // 2
        # Check if the element is present at the middle
        if arr[mid] == target:
            return mid
        # If element is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1

        else:
            # If element is smaller, ignore the right half
            right = mid - 1
    # If we reach here, then the element was not present
    return -1


sortlist = [11, 12, 17, 19, 22, 25, 64]
target = 19
print(binary_search(sortlist, target))

"""
Binary Search is an efficient algorithm for finding a target value within a sorted sequence (usually an array or a list). 
The key idea behind binary search is to repeatedly divide the search interval in half, 
eliminating half of the remaining elements in each step.

-
Binary Search has a time complexity of O(log n), making it very efficient for large datasets compared to linear search.

"""