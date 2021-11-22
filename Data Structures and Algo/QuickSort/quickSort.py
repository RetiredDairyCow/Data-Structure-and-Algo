#Implementation of quick sort. Picking middle element as pivot

# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(arr, low, high):
    pivot = arr[high] #last element
   #J is current element. Every number before J will be divided into two groups:- 
   #less than pivot and greater than pivot. I will always point to the last-
   #number less than the pivot (left sub group)
    i = low - 1 #-1 to start with 
    for j in range(low, high):
       
        if arr[j] < pivot:
            #increment i and swap
            i = i + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    #swap pivot with arr[i+1]     
    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp
    return i+1



def quickSort(arr, low, high):
    if low >= high:    
        return 
    
    newPivotIndex = partition(arr, low, high)
    #at this point newPivot position won't change. So call quicksort for left and right subarray
    quickSort(arr, low, newPivotIndex-1)
    quickSort(arr, newPivotIndex+1, high)
    

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)