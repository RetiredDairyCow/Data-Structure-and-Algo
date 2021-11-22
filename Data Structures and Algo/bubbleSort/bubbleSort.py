#Time Complexity: O(n^2)
#Space Cinokexuty: O(1)
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            #swap
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]


myList = [3,5,19,1,0, 4]
bubbleSort(myList)
print(myList)

