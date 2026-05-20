import sys
class GetNode:
    def __init__(self):

        self.data=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self):
        data=int(input("Enter data: "))
        key=int(input("Enter the key which need to be search"))
        
        newNode=GetNode()
        newNode.data=data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.next is not None:
                if key==ptr.data:
                    break;
                else:
                    ptr=ptr.next

            ptr.next=newNode
            print(data, "is added")
        

    def traverse(self):
        if self.head==None:
            print("Linked List not Present")
        else:
            ptr=self.head
            while ptr!=None:
                print(ptr.data," -> ",end="")
                ptr = ptr.next

    def deleteAtBegin(self):
        pass        


if __name__ == '__main__':
    obj=LinkedList()
    while True:
        print("1. Append")
        print("2. Traverse")
        print("0. Exit")

        n = int(input("Select Any Choice: "))

        if  n==1:
            obj.append()

        elif n==2:
            obj.traverse()

        elif n==0:
            sys.exit()