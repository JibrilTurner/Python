def selectionSort(arr,n):
    for i in range(0,n,1): # runs from the start to end of the loop
        min = i #current min gets set to the index of the current element 
        for j in range(i+j, j < n, 1): #The inner loop runs from the next element to the last element of the array.
            min = j # min gets uodated 
    if min !=i: 
         arr[min], arr[i] = arr[i], arr[min]
    return arr

arr = [88, 74 , 41 , 1 ,63 ,8]
print("Unsorted list:", arr)
selectionSort(arr, 6)
print("Sorted list:", arr)