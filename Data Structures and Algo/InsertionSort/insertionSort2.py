def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i] #key starts with elem at index 1. 
        j = i-1 #starts with assumption that 0th element is sorted
        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        

array = [9, 5 ,1, 4, 3]
insertionSort(array)
print("Array after Insertion sort= " + str(array))