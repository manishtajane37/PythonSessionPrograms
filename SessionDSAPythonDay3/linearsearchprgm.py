def linear_search(n,arr,target):
    flag=False
    for i in range(n):
        if target!=arr[i]:
            flag=False
            # print("search is unsuccessfull")

        else:
            flag=True
            loc=i
            # print("search is successful at ",loc)

    if flag==False:
            print("search is unsuccessfull")

    else:
            print("search is successfull at location",loc)

        
        # if target==arr[i]:
        #     print("search is successful at ",loc)
        # else:
        #     print("search is unsuccessful")



    

if __name__ == "__main__":
    n=int(input("Enter the value of n"))
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    target=int(input("Enter the number which  need to be search"))

    lin
    
    
    ear_search(n,arr,target)    