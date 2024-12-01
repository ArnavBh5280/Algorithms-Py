# IMPLEMENATION OF STACK USING SINGLY LINKED LIST

# 1. Define a class Stack to implement stack data structure using singly linked list concept. Define init () method to initialise start reference variable and item count variable to keep track of number of elements in the stack.
# 2. Define a method is_empty() to check if the stack is empty in Stack class.
# 3. In Stack class, define push() method to add data onto the stack.
# 4. In Stack class, define pop() method to remove top element from the stack.
# 5. In Stack class, define peek() method to return top element on the stack.
# 6. In Stack class, define size() method to retum size of the stack that is number of items present in the stack.

class Node:
    def __init__(self,item,next):
        self.item=item
        self.next=next
        
class Stack:
    def __init__(self):
        self.start=None
        self.item_count=0
        
    def is_empty(self):
        return self.start==None
    
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1
        
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is Empty")
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise self.is_empty()
        
    def size(self):
        return self.item_count
    
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Total elements in the stack= ", s1.size())
print("Top element in the stack= ", s1.peek())
print("Popped elment is= ",s1.pop())
    
        