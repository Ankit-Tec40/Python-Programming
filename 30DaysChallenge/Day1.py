# Date=2-2-2020
# Problem is -------
# Take a list as input and sort it by bubble sort

def bubbleSort(l):
    n = len(l)

    for i in range( n - 1 ) :
        flag = 0

        for j in range(n-i-1) :
            
            if l[j] > l[j + 1] : 
                l[j],l[j + 1] = l[j + 1],l[j]
                flag = 1
        if flag == 0:
            break
    return(l)
lst=[]
size=int(input("Input size of list\n"))
for i in range(size):
    val=int(input())
    lst.append(val)
print(bubbleSort(lst))