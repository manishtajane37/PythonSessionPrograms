num=int(input("Enter the values"))
sum=0
count=0

while num>0 :
    rem=num%10
    sum+=rem
    num=num//10
    count+=1
    
print(sum)   
print(count) 