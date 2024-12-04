# BINARY SEARCH TREE

# 1. Define a class Node with instance variables left, item and right. The vipriables left and right are used to refer left and right child node. The item variable is used to hold data item.
# 2. Define a class BST to implement Binary Search Tree data structure. Make_init__() method to create root instance variable to hold the reference of root node.
# 3. In class BST, define insert method to store new data item in the binary search tree.
# 4. In class BST, define a search method to find a given item in the binary search tree and returns the node reference. It returns None if search failed.
# 5. In class BST, define a method to implement inorder traversal.
# 6. In class BST, define a method to implement preorder traversal.
# 7. In class BST, define a method to implement postorder traversal.

class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
        
class BST:
    def __init_(self):
        self.root=None
        
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data<root.item:
            root.item=self.rinsert(root.left,data)
        elif data>root.item:
            root.right=self.rinsert(root.right,data)
        return root

    def search(self,data):
        return self.research(self.root,data)
    def reesearch(self,root,data):
        if root is None or root.item==data:
            return root
        if data<root.item:
            return self.rsearch(root.left,data)
        else:
            return self.research(root.right,data)
    
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
        
    def prenorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rprenorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
        
    def postnorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostnorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
        

# DELETION IN BINARY SEARCH TREE

# 1. In class BST, define a method to find minimum value item node.
# 2. In class BST, define a method to find maximum value item node.
# 3. In class BST, define a method to delete a node from binary search tree.
# 4. In class BST, define a method size to return the number of elements present in the BST.      

    def min_value(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
            return current.item
        
    def max_value(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
            return current.item
        
    def delete(self,data):
        self.root=rdelete(self.root,data)
        def rdelete(self,root,data):
            if root is None:
                return root
            if data<root.item:
                root.left=self.rdelete(root.left,data)
            elif data>root.item:
                root.right=self.rdelete(root.right,data)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                root.item=self.min_value(root.right)
                self.rdelete(root.right,root.item)
                return root
            
            def size(self):
                return len(self.inorder())
        
        
# b1=BST()
# b1.insert(20)
# b1.insert(100)
# b1.insert(40)
# b1.insert(70)
# b1.insert(15)
# b1.insert(35)
# b1.insert(90)
# print()
