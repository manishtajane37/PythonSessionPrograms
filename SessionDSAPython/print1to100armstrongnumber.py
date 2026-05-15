for i in range(1,10001):
    no=i
    sum=0
    count=0
    save=no

    while no>0:
        no=no//10
        count+=1
    no=save

    while no>0:
        rem=no%10
        sum=sum+(rem**count)
        no=no//10

    if sum==no:
        print("amstrong number :",sum)        