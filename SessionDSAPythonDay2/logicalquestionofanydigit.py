num=(int(input("Enter any value")))
count=0
save=num

while num>0:
    num=num//10
    count+=1
num=save

if count%2==0:
    mid=count//2
    n1=num%10**mid
    n2=num//10**mid

    sum=n1+n2
    sq=sum*sum

print("Number after separation")
print(n1,n2,end=" ")

if sq==save:
    print(save,"number is tech number")
else:
    print(save,"number is not tech")        

