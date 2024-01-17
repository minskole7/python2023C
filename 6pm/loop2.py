# intialization 
#while(condition):
    #statements 
    # increment / decrement


i1 = 1 
while(i1 <= 3):
    print(i1)# 1 # 2 # 3
    i1 = i1 + 1 # 2 # 3 # 4

# print hello 3 types   
i2 = 1
while(i2 <= 3):
    print("hello") # hello # hello # hello
    i2 = i2 + 1 # 2 # 3 # 4

# print 5 to 1 
i3 = 5
while(i3 >= 1):
    print(i3) # 5 # 4 # 3 # 2 # 1
    i3 = i3 -1  # 4 # 3 # 2 # 1 # 0

# print table of 2  
i4 = 2
while(i4 <= 20):
    print(i4) # 2 # 4 ---------------------- 20
    i4 = i4 + 2 # 4 # 6 --------------------22

# print table of 3 
i5 = 3
while(i5 <= 30):
    print(i5)
    i5 = i5 + 3

# print table of 5 in reverse 
i6 = 50
while(i6 >= 5):
    print(i6) # 50 # 45--------------------5
    i6 = i6 - 5 # 45 # 40 -----------------0

i7 = 1
while(i7 <= 5):
    print(i7)  # 1 #2 #3
    if i7 == 3:
        break
    i7 = i7 + 1  #2 #3

i8 = 5
while(i8 >= 1):
    if i8 == 3:
        break
    print(i8) #5 #4
    i8 = i8  - 1 #4  #3

i9 = 1
while i9 <= 5:
    if(i9 == 3):
        i9 = i9 + 1 # 4
        continue
    print(i9) # 1  # 2 # 4 # 5
    i9 = i9 + 1  # 2  # 3 # 5 # 6


for x in range(1,4,-2):
    print(x)