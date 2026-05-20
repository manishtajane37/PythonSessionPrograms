num=int(input("Enter the size of num"))
print("enter list element")
arr=[]

for i in range(num):
    element=int(input())
    arr.append(element)

for i in range(len(arr)):
    print(arr[i])