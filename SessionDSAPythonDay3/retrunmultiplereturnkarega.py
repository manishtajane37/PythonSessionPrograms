def add(a,b):
    res1=a+b
    res2=a-b
    res3=a*b
    return res1,res2,res3

if __name__ == "__main__":
    # add(20,30)
    r1,r2,r3=add(20,30)
    print("addition=",r1)
    print("sub=",r2)

    print("mul=",r3)


