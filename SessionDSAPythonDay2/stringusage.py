# str="my name is enzy amore and i am the certified D and certified that that you can cheat that"
# print(str.find("name"))
# print(str.rfind("r"))

# print(str.count('a'))
# print(str.count('a',2,12))


# print(str.replace("certified","unified"))
# print(str)



str1="Say my name Heisenberg"
res=str1.split()
# print(res)
 
# print(str1[::-1])  
# str1=" ".join(res)
print(str1)
ans=" "

for i in range(len(res)):
    ans=ans + res[i][::-1] +" "    #here res[i] define the words

print(ans)    