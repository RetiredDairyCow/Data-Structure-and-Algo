def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


myList = [3,5,19,1,0, 4]
bubbleSort(myList)
print(myList)
#git not working for some reason
