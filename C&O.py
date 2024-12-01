# CLASSES AND OBJECTS

# __init__method
# It is a type of Instance Method
# Type 1

class Test:
    def __init__(self):
        self.a=2
        self.b=4
        
t1=Test()
t2=Test()
print(t1.a,t1.b)
print(t2.a,t2.b)


# Type 2

class Test:
    def __init__(self,c,d):
        self.a=c
        self.b=d
        
t1=Test(2,3)
t2=Test(4,5)
print(t1.a,t1.b)
print(t2.a,t2.b)


# Instance Object Method

class Test:
    def __init__(self,c,d):
        self.a=c
        self.b=d
    # Instance Method used
    def show(self):
        print(self.a,self.b)  
        
t1=Test(2,3)
t2=Test(4,5)
# Instance Object Called
t1.show() 
t2.show()


# Class Object Method

class Test:
    x=5
    def __init__(self,c,d):
        self.a=c
        self.b=d
    # Class Method Used
    @classmethod
    def f2(cls):
        print(cls.x)
    
        
t1=Test(2,3)
t2=Test(4,5)
# Class Method Called
Test.f2()


# Static Object Method

class Test:
    x=5
    def __init__(self,c,d):
        self.a=c
        self.b=d
    # Static Method Used
    @staticmethod
    def f3():
        print("Hello World")
    # Static method does not access the values
    # of class object and instance object
    # Hence can be used to print a line or text
    # within  the code
    
        
t1=Test(2,3)
t2=Test(4,5)
# Static Method Called
Test.f3()