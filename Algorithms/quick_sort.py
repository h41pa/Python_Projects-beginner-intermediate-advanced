
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left, middle, right = [], [], []

    for x in arr:
        if x <pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)

        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)

my_list = [64, 25, 12, 22, 11, 9]
sorted_list = quick_sort(my_list)
print("Sorted list:", sorted_list)