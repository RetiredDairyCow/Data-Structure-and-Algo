#Time Complexity: O(n*log(n)). Space complexity: O(n)

def merge_Sort(arr):
  if(len(arr) > 1):
    left_array = arr[:len(arr)//2]
    right_array = arr[len(arr)//2:]
  
    merge_Sort(left_array)
    merge_Sort(right_array)

    #merge sorted array
    i = 0 #leftmost element in left array
    j = 0 #leftmost element in right array
    k = 0 #merged array index

    while i < len(left_array) and j < len(right_array):
      if left_array[i] < right_array[j]:
        arr[k] = left_array[i]
        i += 1
        k += 1
      else: 
        arr[k] = right_array[j]
        j += 1
        k += 1

    #transfer remaining into merged array (arr[k])
    while i < len(left_array):
      arr[k] = left_array[i]
      i += 1
      k += 1
    
    while j < len(right_array):
      arr[k] = right_array[j]
      j += 1
      k += 1

myArray = [2,6,5,1,7,4,3]
merge_Sort(myArray)
print(myArray)