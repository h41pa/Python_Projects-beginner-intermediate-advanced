def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
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
