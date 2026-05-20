class Mergesorts:
    def mergesort(self,arr):
        
        if len(arr)>1:
            mid=len(arr)//2

            arr1=arr[:mid]
            arr2=arr[mid:]
            self.mergesort(arr1)
            self.mergesort(arr2)
            j=0
            i=0
            k=0

           

        
        
        while i < len(arr1) and j < len(arr2):

            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i += 1
        
            else:
                arr[k] = arr2[j]
                j += 1

            k += 1
            while len(arr1)>i:


                
                arr[k]=arr1[i]
                i+=1
                k+=1
            while len(arr2)>j:
                arr[k]=arr2[j]
                j+=1
                k+=1

                # return arr

if __name__ == "__main__":
    obj=Mergesorts()
    arr=[11,22,12,24,34,15]
    # arr2=[21,23,15,25]

    obj.mergesort(arr)
    print(arr)
