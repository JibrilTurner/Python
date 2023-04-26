def insertionSort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [88, 74, 41, 1, 63, 8]
print("Unsorted list:", arr)

insertionSort(arr, 6)
print("Sorted list:", arr)
