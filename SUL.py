# IMPLEMENATION OF STACK USING LIST

# 1. Define a class Stack to implement stack data structure using list. Define _init__() method to create an empty list object as instance object member of Stack.
# 2. Define a method is_empty() to check if the stack is empty in Stack class.
# 3. In Stack class, define push() method to add data onto the stack.
# 4. In Stack class, define pop() method to remove top element from the stack.
# 5. In Stack class, define peek() method to return top element on the stack.
# 6. In Stack class, define size() method to return size of the stack that is number of items present in the stack.

class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack Is Empty")
    def size(self):
        return len(self.items)
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top element is: ",s1.peek())
print("Removed element is: ",s1.pop())
print("Top element is: ",s1.peek())
print()