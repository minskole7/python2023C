x = 100
print(x)

#          0          1       2        3      4
names = ["chinmay","sarika","poorva","ram","satish"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])


# program2
#          0       1          2          3        4       5        6
cities = ["pune","mumbai","banglore","kolkata","chennai","goa","jaipur"]
#listname[startIndex:EndIndex(not included):steps]

print(cities[1::])
print(cities[1:5:])
print(cities[1:5:1])


# program 3 
#        0  1  2  3  4  5  6  7  8  9
listA = [11,22,33,44,55,66,77,88,99,100]
print(listA[1:8:2])


#program 4
#        0 1 2 3 4 5 6 7 8 9  10 11 12 13 14 15 16 17 18 19 20 21
listB = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
print(listB[1:21:2])

# program 5
#         0   1  2  3 4  5
listC  = [11,22,33,44,55,66]
print(listC[::-1])
print(listC[4:0:-1])
print(listC[5:1:-1])

# program 6 
fruits = ["apple","mango","banana","orange"]
fruits[0] = "grapes"
print(fruits)

# program 7
print("Mango" in fruits)