import sys
class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=5

    def overfull(self):
        if self.top==self.CAPACITY:
          return True
        else:
           return False

    def underflow(self):

        if self.top==-1:
             return True

        else:
          return  False             

    def push(self,ele):

        if self.overfull():
            print("Stack is overflow can't insert value")
        else:
            self.top=self.top+1
            self.stack.append(ele)

    def traverse(self):
        if self.underflow():
            print("Stack is empty")      
        else:
            for i in range(self.top,-1,-1):
                print(self.stack[i])


    def pop(self):
        if self.underflow():
            print("stack is empty can't delete")
        else:
            ele=self.stack[self.top]    #here we have store the element which is going to be delete
            self.stack.pop()  #delete the last element 
            self.top=self.top-1                ##vaha top tha ab element delete hogaya hai soo backward



if __name__== "__main__":
    obj=Stack()
    while True:
        print("1 for Insertion")
        print("2 for deletion")
        print("3 for Traversing")
        
        ch=int(input("Enter you choice"))
        if ch==1:
            ele=int(input("ENter the value"))
            obj.push(ele)
        elif ch==2:
            obj.pop()
        elif ch==3:
            obj.traverse()
        elif ch==0:
            sys.exit(0)    


        





        
        