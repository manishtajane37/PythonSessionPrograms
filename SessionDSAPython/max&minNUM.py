
arr=[20,40,60,33,23,99]
max=arr[0]
min=arr[0]
for i in range(len(arr)):
   if max<arr[i]:
        max=arr[i]
        
print(max)  

for i in range(len(arr)):
    if min>arr[i]:
        min=arr[i]
print(min)        