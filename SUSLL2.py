# IMPLEMENATION OF STACK BY IMPORTING SINGLY LINKED LIST MODULE

# 1. Import module containing singly linked list code in your python file.
# 2. Define a class Stack to implement stack data structure. Define init () method to create Singly Linked List (SLL) object.
# 3. Define a method is_empty() to check if the stack is empty in Stack class.
# 4. In Stack class, define push() method to add data onto the stack.
# 5. In Stack class, define pop() method to remove top element from the stack.
# 6. In Stack class, define peek() method to return top element on the stack.
# 7. In Stack class, define size() method to return size of the stack that is number of Items present in the stack.

from SLL import *

class Stack:
    def __init__(self):
        self.myList=SLL
        self.item_count=0
        
    def is_empty(self):
        return self.myList.is_empty()
    
    def push(self,data):
        self.myList.insert_at_start(data)
        self.item_count+=1
        
    def pop(self):
        if not self.is_empty():
            self.myList.delete_first()
            self.item_count-=1
        
            
    def peek(self):
        if not self.is_empty():
            return self.myList.start.item
        
    def size(self):
        return self.item_count()
        
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top element is ", s.peek())
s.pop()
print("Top element is ", s.peek())
print()


# ERROR IN CODE.....CHECK KRNA PDEGA
