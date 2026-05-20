import sys
class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=-1
        self.front=0
        self.CAPACITY=5

    def isFull(self):
        if self.rear==self.CAPACITY-1:
            return True
        else:
            return False

    def insert(self,ele):
        if self.isFull():
            print("queue is full")
        else:
            self.rear=self.rear+1
            self.queue.append(ele)
            print("ele is inserted")


    def traverse(self):
        if self.isEmpty():
            print("queue is Empty")
        else:
            for i in range(self.rear+1):
                print(self.queue[i])



                


    def isEmpty(self):
        if self.rear==-1:
            return True
        else:
            return False
    
          

    def delete(self):

        if self.isEmpty():
            print("Queue is empty")
        else:
            ele=self.queue[self.front]
        for i in range(1,self.rear+1):
         
            self.queue[i-1]=self.queue[i]
            self.rear-=1   

        return ele 
        
        for i in range():
         if self.isEmpty():
            print("Stack is Empty")
        else:
            ele = self.stack.pop()
            self.top = self.top - 1
            return ele
        
    
    def peek(self):
        if self.isEmpty():
            print("queue is Empty")
        else:            
            print(self.queue[self.rear])


class stacks:

    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 5

    def isFull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, ele):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top = self.top + 1
            self.stack.append(ele)
            print(ele, "is pushed")

    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            ele = self.stack.pop()
            self.top = self.top - 1
            return ele

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Top element is:", self.stack[self.top])


    def traverse(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Stack elements are:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])


if __name__ == '__main__':
    obj=Queue()
    obj1=stacks()
    for i in range(obj.CAPACITY):
        ele=int(input("Enter value"))
        obj.insert(ele)

    for x in range(obj.CAPACITY):
        ele=obj1.delete()
        obj1.push(ele) 
        # self.stack.append(ele)
        # print(ele, "is pushed")

    for x in range(obj.CAPACITY):    
        ele=obj1.pop()
        obj1.insert(ele)

    obj1.traverse()    



    



    # while True:
    #     print("1. insert")
    #     print("2. delete")
    #     print("3. Peek")
    #     print("4. Traverse")
    #     print("0. Exit")
    #     ch=int(input("select any choice"))
    #     if ch==1:
    #         ele=int(input("Enter data: "))
    #         obj.insert(ele)
    #     elif ch==2:
    #         obj.delete()
    #     elif ch==3:
    #         obj.peek()
    #     elif ch==4:
    #         obj.traverse()
    #     elif ch==0:
    #         sys.exit(0)