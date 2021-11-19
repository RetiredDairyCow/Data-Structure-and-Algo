#Insertion Sort Time Complexity: O(n^2). Space Complexity: O(1) (no new space is needed/created)

def insertionSort(array):
    for i in range(1, len(array)):
        currentElement = array[i]
        j = i-1
        while j >= 0 and currentElement <= array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = currentElement

myArray = [3, 2, 1, 15, 9]
insertionSort(myArray)
print(myArray)