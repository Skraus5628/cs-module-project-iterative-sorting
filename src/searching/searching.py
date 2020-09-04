def linear_search(arr, target):
    # Your code here
    
    #Search the index of the whole length of the array
    for i in range(len(arr)):
        #if the array index is equal to the target return that index
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here

    #Set low to the start of the array
    low = 0
    #Set high to the final index of the array
    high = len(arr) -1

    #As long as the low is less than or equal to the high value set middle to the median (low+high/2)
    while low <= high:
        middle = (low + high) // 2
  
        # IF the middle index of the array is the target, return the middle index
        if arr[middle] == target:
            return middle
        #IF it isnt
        else:
            # if the middle index of the array is greater than the target
            if arr[middle] > target:
                #Set the high index to the middle of the array -1 (searches to the left of the middle)
                high = middle - 1
            else:
                #if its less than the target, set the low index to middle + 1 (searches to the right of the middle)
                low = middle + 1


    return -1  # not found
