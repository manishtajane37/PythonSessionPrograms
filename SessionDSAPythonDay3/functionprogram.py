def add(num1,num2):
    res=num1*num2
    return res       #we don't write return in without return print the msg here "print("output",res)"
          #in java C++ return num1,num2,num3 is not allow but it is allow in java

   

# if __name__ == "__main__" :
#     num1=int(input("enter the value of num1"))
#     num2=int(input("enter the value of num2"))
    
#     add(num1,num2)                 without return 

if __name__ == "__main__" :
    num1=int(input("enter the value of num1"))
    num2=int(input("enter the value of num2"))
    r=add(num1,num2)
    print("output=",r)       #with using return 


