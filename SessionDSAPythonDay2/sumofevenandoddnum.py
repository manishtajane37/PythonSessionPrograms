n=int(input("Enetr the value of n"))
print("Enter element")
arr=[]
even=0
odd=0
e1count=0
odcount=0

for i in range(n):
    ele=int(input())
    arr.append(ele)

for i in range(len(arr)):
    if(arr[i]%2==0):
        even+=arr[i]
        e1count+=1
      
    else:
        odd+=arr[i]
        odcount+=1
print("Even sum =", even)
print("Even count =", e1count)

print("Odd sum =", odd)
print("Odd count =", odcount)

    
    
    
