def binary_search(n,arr,target):
    flag=False
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if target==arr[mid]:
            flag=True
            loc=mid
            break

        elif target<arr[mid]:
             high=mid-1


        elif target>arr[mid]:
             low=mid+1     
         
        
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


    
    
    binary_search(n,arr,target)    