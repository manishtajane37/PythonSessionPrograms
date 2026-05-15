num=int(input("Enter the value"))
fact=1
sum=0
save=num              #you can use it for rem also --temp=rem
while num>0:
    rem=num%10
    fact=1
    
    while rem>0:    
        fact*=rem
        rem-=1
        
    sum+=fact
    num=num//10

if save==sum:
    print("value is peterson")
else:
    print("value is not peterson")    



    

   
