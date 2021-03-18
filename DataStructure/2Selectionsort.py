def selectionsort(lst):
    n=len(lst)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if lst[j]<lst[min]:
                min=j
        lst[i],lst[min]=lst[min],lst[i]
    return(lst)
            


lst=[4,8,2,14,9,6,3,7,1,5,41,21,54,12]
print(selectionsort(lst))
