import sys

class stacks:

    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 5

    # Check stack is full
    def isFull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False

    # Check stack is empty
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    # Push operation
    def push(self, ele):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top = self.top + 1
            self.stack.append(ele)
            print(ele, "is pushed")

    # Pop operation
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            ele = self.stack.pop()
            self.top = self.top - 1
            return ele

    # Peek operation
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Top element is:", self.stack[self.top])

    # def reversearray(self,arr):
    #     for i in arr:
    #         self.push()
    #         reverse_arr=[]
    def traverse(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Stack elements are:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])


if __name__ == '__main__':

    obj = stacks()
    arr=[1,2,3,4,5]
    rev=[]
    for i in range(len(arr)):
        obj.push(arr[i])
    
    for i in range(len(arr)):
        ele=obj.pop()
        rev.append(ele)
    print(ele)        

    while True:

        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        ch = int(input("Select any choice: "))

        if ch == 1:
            ele = int(input("Enter element: "))
            obj.push(ele)

        elif ch == 2:
            ele = obj.pop()
            if ele is not None:
                print(ele, "is popped")

        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.traverse()

        elif ch == 0:
            print("Program Ended")
            sys.exit()

        else:
            print("Invalid Choice")