lst=[3,2,4,1,6,8,5]
n=len(lst)
for i in range (1,n):
    val=lst[i]
    j=i-1
    while j>=0 and lst[j]>val:
        lst[j+1]=lst[j]
        j=j-1
    lst[j+1]=val

print(lst)
