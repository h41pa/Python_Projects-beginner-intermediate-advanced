
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
            right = mid -1
    # If we reach here, then the element was not present
    return -1


sortlist = [11, 12, 17, 19, 22, 25, 64]
target = 19
print(binary_search(sortlist, target))
