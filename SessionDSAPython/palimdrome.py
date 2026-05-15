num=int(input("Enter the values"))
rev=0
save=num

while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10

if rev==save:
    print("number palimdrome")
else:
    print("number is palimdrome")    
