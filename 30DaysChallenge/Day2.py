# Date=12-2-2020
# Selection sort

def Selectionsort(l):
    n=len(l)
    for i in range(n):
        minindex=i
        for j in range(i+1,n):
            if(l[j]<l[minindex]):
                minindex=j
        l[i],l[minindex]=l[minindex],l[i]
    return(l)

lst=[7,5,6,8,9,1,3,5,56,5,2,5,54,54,6]
#size=int(input("Input size of list\n"))
#for i in range(size):
  #  val=int(input())
  #  lst.append(val)
print(Selectionsort(lst))

