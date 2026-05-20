num=input("Enter you mobile number")
# isdigit()
# if num[0]=6 or num[0]=7 or  num[0]=7 or  num[0]=7:
# for i in range(11):
if num.isdigit():
        if len(num)==10:
            if num.startswith("6") or num.startswith("7") or  num.startswith("8") or num.startswith("9"):
                print("Number is valid")
            else:
                  print("Enter valid mobile number")   #if no. don't start with 6 7  8 9
        else:
                  print("Mobile number must be 10 digits")       #digit should be 10 else this will print             
    

    
else:
        print("not in digit format")   #must be number
            

  

