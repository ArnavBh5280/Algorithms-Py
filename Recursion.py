# Problems based on RECURSION

# 1. Write a recursive function to print first N natural numbers.
# 2. Write a recursive function to print first N natural numbers in reverse order.
# 3. Write a recursive function to print first N odd natural numbers.
# 4. Write a recursive function to print first N even natural numbers
# 5. Write a recursive function to print first N odd natural numbers in reverse order.
# 6. Write a recursive function to print first N even natural numbers in reverse order.

def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=' ')
printN(10)
print() #prints a blank line

def printNrev(n):
    if n>0:
        print(n,end=' ')
        printNrev(n-1)
printNrev(10)
print()

def printNodd(n):
    if n>0:
        printNodd(n-1)
        print(2*n-1,end=' ')
printNodd(10) 
print()

def printNeven(n):
    if n>0:
        printNeven(n-1)
        print(2*n,end=' ')
printNeven(10)  
print()

def printNoddrev(n):
    if n>0:
        print(2*n-1,end=' ')
        printNoddrev(n-1)
printNoddrev(10)
print()

def printNevenrev(n):
    if n>0:
        print(2*n,end=' ')
        printNevenrev(n-1)
printNevenrev(10) 
print()

   
# 1. Write a recursive function to calculate sum of first N natural numbers.
# 2. Write a recursive function to calculate sum of first N odd natural numbers
# 3. Write a recursive function to calculate sum of first N even natural numbers
# 4. Write a recursive function to calculate factorial of a number.
# 5. Write a recursive function to calculate sum of squares of first N natural numbers.     

def f(n):
    if n==1:
        return 1
    return n+f(n-1)
print(f(10))
print()

def f1(n):
    if n==1:
        return 1
    return (2*n-1)+f1(n-1)
print(f1(10))
print()

def f2(n):
    if n==1:
        return 1
    return (2*n)+f2(n-1)
print(f2(10))
print()
    
def f3(n):
    if n==0:
        return 1
    return n*f3(n-1)
print(f3(10))
print()
    
def f4(n):
    if n==1:
        return 1
    return (n*n)+f4(n-1)
print(f4(10))
print()
    




        