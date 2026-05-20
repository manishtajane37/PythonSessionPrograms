# str=input("Enter any given string")
str="aabbccddeeffaa"

s=set(str)
print(s)




s = "AABBCCDDEE"
result = ""

for ch in s:   #here ch ek eke letter honga joh repeat 
    if ch not in result:  #agar ch means woh letter result mai nhi hai toh add karo else maat
        result += ch

print(result)