arr=[]
n=int(input("Enter the value of n"))
for i in range(n):
    arr.append(int(input("Enter number :")))

key=int(input("Enter the Element which need to be insert"))
loc=int(input("Enter the location"))
arr.append(0)

for i in range(len(arr)-1,loc,-1):
    arr[i]=arr[i-1]
arr[loc]=key
print(arr)

for i in range(loc+1):
    arr[i-1]=arr[i]
# arr.pop()
print(arr)    