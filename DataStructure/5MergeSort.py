def mergesort(lst):
    if len(lst)>1 :
        mid=len(lst)//2
        Llst=lst[0:mid]
        Rlst=lst[mid:]
        mergesort(Llst)
        mergesort(Rlst)
        i=0
        j=0
        k=0
        while i<len(Llst) and j<len(Rlst):
            if(Llst[i]<Rlst[j]):
                lst[k]=Llst[i]
                i=i+1
                k=k+1
            else:
                lst[k]=Rlst[j]
                j=j+1
                k=k+1
        while i<len(Llst):
            lst[k]=Llst[i]
            i=i+1
            k=k+1
        while j<len(Rlst):
            lst[k]=Rlst[j]
            j=j+1
            k=k+1
    return(lst)



lst=[6,1,9,3,7,5,4,10,18,85,42,99,81,45,11]
print(mergesort(lst))
