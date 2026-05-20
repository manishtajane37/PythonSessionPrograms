num=int(input("Enter any six digit number"))
save=num
num1=num%100
num=num//100
num2=num%100
num=num//100
num3=num%100

sum=num1+num2+num3
mul=sum*sum*sum
print("Number after separation")
print(num3,num2,num1,end=" ")

if mul==save:
    print(save,"number is tech number")
else:
    print(save,"number is not tech")        

