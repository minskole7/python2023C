print(1)
print(2)
print(3)
print(4)
print(5)


# for loop and while 
#range(startIndex,endIndex(not included),steps)

# print 0 to 4
for x in range(5):
    print(x)

# print 1 to 5 
for x in range(1,6):
    print(x)

# print "hello"  3 times
for x in range(3):
    print("hello")

# print 1 to 10 
for x in range(1,11,1):
    print(x)

# print table of 2 
#2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
for x in range(2,21,2):
    print(x)

# print table of 5     
for x in range(5,51,5):
    print(x)

# print table of of 5 in reverse
for x in range(50,4,-5):
    print(x)

# print table of 3 in reverse 
for x in range(30,2,-3):
    print(x)

# for with break statement 
for x in range(10):
    if x == 5:
        break 
    print(x) # 0 1 2 3 4

for x in range(10):
    print(x)  # 0 1 2 3 4 5
    if x == 5:
        break 

for x in range(10,1,-2):
   if x == 4:
       break
   print(x)

# continue with for 
   
for x in range(1,6,1):
    if x == 2:
        continue
    print(x) # 1 # 3 # 4 # 5

for x in range(30,3,-3):
    if x == 15:
        continue
    print(x)


# while loop
    
# intialization    
#while(condition):
    # statement
    # increment / decrement

i1 = 1
while(i1 <= 5):
    print(i1) # 1 # 2 # 3 # 4 # 5
    i1 = i1 + 1 # 2 # 3 # 4 # 5 # 6

i2 = 5 
while(i2 >= 1):
    print(i2) #5 # 4 # 3 # 2 # 1
    i2 = i2 - 1 # 4 # 3 # 2 # 1 # 0

i3 = 2
while(i3 <= 20):
    print(i3) # 2 # 4 ----------- 20
    i3 = i3 + 2 # 4 # 6---------22

i4 = 50
while(i4 >= 5):
    print(i4)
    i4 = i4 - 5
    







