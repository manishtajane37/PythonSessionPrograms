arr=[]
n=int(input("Enter the value of n"))
for i in range(n):
    arr.append(int(input("Enter number :")))

key=int(input("Enter the Element which need to be insert"))
loc=int(input("Enter the location"))
arr.append(0)
# arr[i]=arr[i-1]                   #this code for replace the input
arr[loc]=key
# print(arr[loc])

for i in range(n):
    print(arr[i])