num=int(input("Enter any four digit number"))
num1=num%100
num2=num//100

sum=num1+num2
mul=sum*sum
print("Number after separation")
print(num2,num1)

if mul==num:
    print("number is tech number")
else:
    print("number is not tech")        

