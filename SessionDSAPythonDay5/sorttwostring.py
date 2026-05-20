Str1="arra"
Str2=" "
for i in Str1:
    if i.isalpha():
        Str2=Str2+i


print(Str2)        
Str2=Str2.lower()
rev=Str2[::-1]
if rev==Str2:
    print("palimdrome")
else:
    print("Not a palimdrome")    