print("hello")

# day 1 

x = 10
print(x)
x = 100
print(x)

# Arithmetic operation - + , - , * , / ,%

q = 8 
r = 4

print(q+r)
print(q-r)
print(q*r)
print(q/r)
print(q%r)  # remainder

a = 10 
b = 5 

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)


# function 

def Calculator(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)
Calculator(12,3)
Calculator(6,3)



# function without parameter and without return type 
def add():
    print(9+9)
add()
add()
add()
add()
add()

# function with parameter and without return type 
def addB(x,y):
    print(x+y)
addB(12,3)
addB(1,3)
addB(11,5)

# function with parameter and with return type 
def addC(x,y):
    return x + y

q1 = addC(1,3)
print(q1)
print(q1 + q1)
print(q1 - 1)


# Type 

# int
x = 10 
print(x)
print(type(x))
# 10 , - 10 , 0

#float
h = 10.5
print(h)
print(type(h))
# 10.5 , -10.7 , 0.0

# boolean
n = True
print(n)
print(type(n))
# True or False

#string
q = 'chinmay'
print(q)
print(type(q))
# 'chinmay','a','1','32de#@#$',' '


# comparison operator ===> boolean ====> True or False
# < , > , <= , >= , != , ==

a = 10 
b = 5

print(a > b)
print(7 > 3) # True
print(7 < 3) # False
print(7 >= 3) # True
print(7 <= 3) # False
print(7 <= 7)  # True
print(7 >= 7) # True
print(7 != 6) # True
print(7 == 6) # False
print(7 == 7) # True

# Logical operator
# and #or  #notoperator 


# and 
# True  and  True  =====>  True 
# True  and  False  =====> False 
# False and  True  =====>  False 
# False and  False  =====> False 

print(2 == 2 and 3 == 3) # True 
print(2 == 2 and 3 != 3) # False
print(2 != 2 and 3 == 3) # False 
print(2 != 2 and 3 != 3) # False

#or operator
# True  or  True  =====>  True 
# True  or  False  =====> True 
# False or  True  =====>  True 
# False or  False  =====> False 

print(3 == 3 or 4 != 5)
print(3 == 3 or 4 == 5)
print(3 != 3 or 4 != 5)
print(3 != 3 or 4 == 5)

# not operator
print(not (8 == 8))
print(not (8 != 8))





































