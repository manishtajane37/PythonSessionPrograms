num=int(input("Enter any number"))
sum=0
save=num

count=0
while num>0 :
   
    num=num//10
    count+=1

num=save   

while num>0:
    rem=num%10
    sum=sum+(rem**count)
    num=num//10


    

if(sum==save):
    print("number is armstrong")
else:
    print("number is not armstrong ")  

   