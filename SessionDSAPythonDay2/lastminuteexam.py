rec={}
n=int(input("Enter the number of any student"))

for i in range(n):
    name=input("Say my name")
    per=float(input("enter perc :"))
    rec[name]=per
print(rec)
for x in rec:
    print(x,"\t",rec[x])    