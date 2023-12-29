
# conditional statements 

# one input and multiple outcomes , then we will use conditional statements 

# Music concert 
# numT > 0 and numT <= 5   ===> 5 % discount
# numT > 5 and numT <= 10  ===> 10 % disocunt 
# numT > 10                ===> 20 % discount

# if condition:
#     #statement will be executed


numT = 17
if numT > 0 and numT <= 5:
    print("5 % discount")
if numT > 5 and numT <= 10:
    print("10 % discount")
if numT > 10:
    print("20 % discount")

#if elif else

numT2 = -17

if numT2 > 0 and numT2 <= 5:
    print("5 % discount")
elif numT2 > 5 and numT2 <= 10:
    print("10 % discount")
elif numT2 > 10:
    print("20 % discount")
else:
    print("incorrect input")

# program 3
    
marks = 55
# if marks > 90:
#     print("Grade A")
# if marks >= 75:
#     print("Grade B")
# if marks >= 65:
#     print("Grade C")

if marks > 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 65:
    print("Grade C")
else:
    print("Please try again....")


# program 4
s = 10
t = 50

if s > t:
    print("s is greater")
else:
    print("t is greater")

# program 5
    
x1 = 10 
x2 = 50
x3 = 100

if x1 > x2 and x1 > x3:
    print("x1 is greater")
elif x2 > x1 and x2 > x3:
    print("x2 is greater")
else:
    print("x3 is greater")

# program 6
h = 10 
i = 50

if h > i :
    print("h is greater")
else:
    print("i is greater")

print("h is greater") if h > i else print("i is greater")

age = 17
q1 = "can drive" if age >= 18 else "cannot drive"
print(q1)


# loops

print(1)
print(2)
print(3)
print(4)
print(5)


# for loop with range() function
#for x in range(startIndex, EndIndex(not included),Steps):
    # statements
#default startIndex is 0

for x in range(10):
    print(x)

for x in range(1,10):
    print(x)

for x in range(1,6):
    print(x)

# 2 3 4 5 6 7 8 10 11 12 13 14 15 16 17 18 19 20
for x in range(2,21,2):
    print(x)

for x in range(3,31,3):
    print(x)

for x in range(50,0,-5):
    print(x)










































