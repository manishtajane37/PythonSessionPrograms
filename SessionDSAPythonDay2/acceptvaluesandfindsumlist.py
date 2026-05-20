n=int(input("Enetr the value of n"))
print("Enter element")
arr=[]
sum=0

for i in range(n):
    ele=int(input())
    arr.append(ele)

for i in range(len(arr)):
    
    sum+=arr[i]
    print(sum,end=" ")
    
