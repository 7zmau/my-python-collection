def binarySearch(theList, x):
    high = len(theList)-1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if theList[mid] == x:
            return True
        elif x < theList[mid]:
            high = mid - 1
        else:
            low = mid + 1
        
    
