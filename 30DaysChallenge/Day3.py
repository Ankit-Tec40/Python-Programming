# Date=13-2-2020
# Insertion Sort

arr=[54,43,5,456,4,453,568,6,54685,65,54,6,586,596565,65,6565,64465,456,454,5,45,45,45,4,5]


for i in range(1, len(arr)):  
    key = arr[i] 
    j = i-1
    while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
    arr[j+1] = key
    
print(arr)
print(arr)
print(arr)