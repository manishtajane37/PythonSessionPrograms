# str1="hello"
str1=input("ENter anu string ")
reverse=" "
# for i in str1:  #this use krteh toh bss reverse=i + reverse likhteh 
for i in range(len(str1)):
    reverse=str1[i]+reverse     #len(str1) 0 1 2 3 ke form mai len count krta hai isliey str1[i]+ reverser likhe vrrma 
print(reverse)    

