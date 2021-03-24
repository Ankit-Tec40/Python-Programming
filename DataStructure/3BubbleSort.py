lst=[3,2,4,1,6,8,5,7]
n=len(lst)
for i in range(0,n-1):
    flag=0
    for j in range(0,n-i-1):
        if (lst[j]>lst[j+1]):
            lst[j],lst[j+1]=lst[j+1],lst[j]
            flag=1
    if flag==0:
        break

print(lst)