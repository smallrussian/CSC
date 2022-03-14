def InsertionSort(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=1-1
        while j>0:
            if arr[j]<arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
            j-=1
            #print(arr)
    print(arr)
    return arr
#i had minuses at first so i used geeks for geeks 
def InsertionSort2(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)
    return arr

def SelectionSort(arr, n):
    for i in range(n):
     
    # Find the minimum element in remaining
    # unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
             
    # Swap the found minimum element with
    # the first element       
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
    

def BubbleSort(arr, n):
    for i in range(n):
        swapped=False
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                swapped=True
        if swapped==False:
            break
    print(arr)
    return arr  

def SelectionSearch(arr, what):
    #go through the entire array and see if each element is what you are looking for 
    for i in range (0, len(arr)):
        if what==arr[i]:
            return i
    return -1

def BinarySearch(arr, low, high, x):
    if high>=low: #lines 58 and 67 feel redundant
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return(BinarySearch(arr, low, mid-1, x))
        else:
            return(BinarySearch(arr, mid+1, high, x))
    else:
        return -1

def GeeksbinarySearch (arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
         
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return GeeksbinarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
        else:
            return GeeksbinarySearch(arr, mid + 1, r, x)
 
    else:
        # Element is not present in the array
        return -1


#main program
#test2=[5,4,6,2,3,1]
#testArray=["Lockhart", "Quirrell", "Crouch", "Umbridge", "Hooch", "Trelawney", "Slughorn", "Snape", "Sprout", "Flitwick", "Hagrid", "Sinistra"]
#findIt=str(input("Who should I find?\n"))
#BubbleSort(testArray, len(testArray))#
#location=BinarySearch(testArray, 0, len(testArray)-1, findIt)
#location=GeeksbinarySearch(testArray, 0, len(testArray)-1, findIt)
#print("What you want is at position " + str(location))
#print("Insertion Sort")
#InsertionSort2(testArray)
#print("Selection Sort")
#SelectionSort(test2, len(test2))
#print("bubble sort")
#BubbleSort(testArray, len(testArray))
