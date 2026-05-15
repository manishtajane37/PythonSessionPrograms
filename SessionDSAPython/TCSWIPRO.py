cost_price=int(input("Enter the cost price"))
Category_name=input("Enter the category")

if Category_name=="student" and cost_price>500:
    discount=(cost_price/10)*100
else:
    discount=(cost_price/5)*100    

if Category_name!="student" and cost_price>500:
    discount=(cost_price/8)*100
else:
    discount=(cost_price/2)*100

net=cost_price-discount
print(cost_price)
print(discount)       
print(net)