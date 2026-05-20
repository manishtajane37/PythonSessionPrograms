arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4,]

arr3 = []   

for i in arr1:
    if i in arr2:
        arr3.append(i)

print("Common elements:", arr3)