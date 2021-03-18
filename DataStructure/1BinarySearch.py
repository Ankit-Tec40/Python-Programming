# it works on sorted array
    # 1 recursive method
def BinarySearch(lst,low,high,val): 
    middle=int((low+high)/2)
    if (lst[middle]==val):
        return middle
    elif(lst[middle]>val):
        return BinarySearch(lst,low,middle-1,val)
    elif(lst[middle]<val):
        return BinarySearch(lst,middle+1,high,val)
    else:
        return -1

    # 2 Iterative method
def BinarySearch_I(lst,low,high,val):
    mid=int((low+high)/2)
    while mid<=high :
        if lst[mid]==val:
            return mid
        elif lst[mid]>val:
            high=mid-1
        elif lst[mid]<val:  
            low=mid+1
        else:
            return -1
 

lst=[4,5,7,8,9,11,14,19,25]
ar=BinarySearch(lst,0,len(lst)-1,11)
ai=BinarySearch(lst,0,len(lst)-1,14)
print("Found at",ar,"and",ai)