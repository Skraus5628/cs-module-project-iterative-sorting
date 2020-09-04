# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for cur_index in range(0, len(arr) -1):
        # setting smallest index to current index
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        
        #looping over numbers in the range of the current index(smallest) starting at +1 (next node from smallest)
        # Then going the length of the array
        for num in range(cur_index +1, len(arr)):
            #if the number is less than the smallest index, set smallest index to that number
            if arr[num] < arr[smallest_index]:
                smallest_index = num 
                
        # TO-DO: swap
        # Your code here
        
        # current index, smallest index ----> becomes smallest index, current index
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    #Go through all array elements

     #last i elements are in place
    for i in range(n-1):
        for j in range(0, n-i-1):
         #go through array from 0 to n-i-1
            if arr[j] > arr[j+1] :
                #Swap if element found is greater than next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
#Time comp: O(n + maximum)
#Space comp: O(n + maximum)
#O(n) simplified for both

def counting_sort(arr, maximum=None):
    # Your code here
    
    # If the length of the array is less than 2 no sorting needed, return array
    if len(arr) < 2:
        return arr

    # If the maximum is set to none, set maximum to the largest value in the array
    if maximum is None:
        #TC: 0(n)
        maximum = max(arr)

        #set buckets equal to first index multiplied by the maximum array vavlue +1
    buckets = [0] * (maximum + 1)

    #loop thru array elements
    for elem in arr:
        # if the element is less than 0 throw an error and shame the user
        if elem < 0:
            return "Error, negative numbers not allowed in Count Sort"
        #Increase the bucket element count by 1
        buckets[elem] += 1
    
    #set index to position 1
    i = 0
     
     #loop over bucket index within range of max +1
    for bucket_index in range(maximum + 1):
        #loop over the bucket indexes within the buckets
        for _ in range(buckets[bucket_index]):
            #array indexes starting at 0 = bucket index
            arr[i] = bucket_index
            #increase array index by 1
            i += 1    
    
    return arr
