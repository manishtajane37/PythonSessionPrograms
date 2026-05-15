num=int(input("enter any 4 digit no."))

n1=num%10

num=num//10
n2=num%10

num=num//10
n3=num%10

num=num//10
n4=num%10

res=n1*1000+n2*100+n3*10+n4*1
print(res)





