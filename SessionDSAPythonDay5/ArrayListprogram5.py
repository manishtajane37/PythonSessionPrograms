# arr1=[]
# arr2=[]
# arr3=[-1,2,3,-4,-5,6]

# for i in range(len(arr3)):
#     if arr3[i]<0:
#         arr2.append(arr3[i])
#     else:
#         arr1.append(arr3[i])  

# # for i in range(len(arr3)):        

# print("Posivitive number:",arr1)
# print("Nagative number:",arr2)








#Below we have taken user input 





posarray=[]
negarray=[]
array1=[]
n=int(input("Enter the value of n"))

for num in range(n):
    ele=int(input("Enter the element inside the array"))
    array1.append(ele)
print(array1)    

for num in array1:
    if num<0:
        negarray.append(num)
    else:
        posarray.append(num)

print("Positive values=",posarray)
print("Nagative values=",negarray)
