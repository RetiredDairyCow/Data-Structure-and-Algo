#Selection sort time complexity: O(n^2). Space complexity: O(1)
def selectionSort(arr):
    
    for i in range(len(arr)):
        currentMin = arr[i]
        for j in range(i, len(arr)):
            if(arr[j] < currentMin):
                minIndex = j
                currentMin = arr[j]
        #swap i and elem at minIndex
        if currentMin < arr[i]:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
                
#driver code
myArray = [20, 12, 10, 15, 2]
selectionSort(myArray)
print(myArray)