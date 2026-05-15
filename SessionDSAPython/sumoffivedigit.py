
num=int(input("Enter the any five digit num"))
n1=num%10

num=num//10
n2=num%2

num=num//10
n3=num%10

num=num//10
n4=num%10

num=num//10
n5=num%10

res=n1+n2+n3+n4+n5
print(res)