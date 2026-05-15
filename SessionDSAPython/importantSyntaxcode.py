ls=[]     #syntax for list
print(type(ls))   #class<list> 
ls=list()
ls=[1,2,3,4,5,6]
print(type(ls))
# three ways for creating list


arr=[1,2,3,4,5,6,7,8,9,10]


print(arr[-1])    #value will be 6
print(arr[1:3])
print(arr[:6])      # 1 to 6
print(arr[3:])  # 4 to 10



print(arr[::2])   # 1 3 5 7 9
print(arr[::-1])   #use for reverse
print(arr[::-2])   #reverse in gap of 2

print(arr[2::])    # 1 and 2 ke 3,4,5,6,7,8,9,10
