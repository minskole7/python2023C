# how to define variable 
# arithmetic operation
# comparison operator 
# logical operator
# conditional statements 
# loops

# collections -  string , list , dictionary , set , tuple 

# list 

#          0         1        2       3
names = ["sameer","sarika","satish","ram"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# program 2
# list of numbers 
#          0  1  2  3  4
numbers = [11,22,33,44,55]
print(numbers[0])

# for loop - 2 and while loop
# loop over a list 
#           0       1        2          3
cities = ["pune","mumbai","banglore","kolkata"]
print(len(cities))
# range(startIndex:endIndex(not included):stepSize)
for x in range(len(cities)):
    #print(x)
    print(cities[x])

#            0        1           2        3
country = ["india","pakistan","srilanka","cuba"]
for x in range(len(country)):
    #print(x)
    if x != 2:
        print(country[x])


# program looping over a list without using range function 
country = ["india","pakistan","srilanka","cuba"]  
for z in country:
    if z != "srilanka":
        print(z)


# program 4 - while loop 
#            0      1       2         3        4  
fruits = ["apple","mango","banana","grapes","papaya"]  
t1 = 0

while(t1 < len(fruits)):
    #print(t1)
    print(fruits[t1])
    t1 = t1 + 1


# program 5
# Check whether a particular element exist in list 
states = ["MH","MP","UP","RJ"]
print("Mp" in states)
if "MP" in states:
    print('city found')
else:
    print('city not found')

#program 6
#How to update a list element 
vegetables = ["carrot","brinjal","tomato","potato"]
vegetables[2] = "cauliflower"
print(vegetables)

# program 7 - properties and methods on list

# append()
vegetables = ["carrot","brinjal","tomato","potato"]
vegetables.append("ladyfinger")
print(vegetables)

#pop()
vegetables.pop()
print(vegetables)
#remove the element by index
vegetables.pop(1)
print(vegetables)

#count()
numbers = [11,22,33,44,55,66,77,55,44,44,56,44]
q1 = numbers.count(44)
print(q1)

for item in range(len(numbers)):
    if numbers[item] == 44:
        print(item)

# clear()
animals = ["lion","tiger","rabbit","bear"]
animals.clear()
print(animals)

# program 8
animals = ["lion","tiger","rabbit","bear"]
animals.extend(['snake','frog'])
print(animals)

listA = [11,22,33]
listB = [44,55,66]
listB.extend(listA)
print(listB)

# index
q3 = animals.index('rabbit')
print(q3)

# remove
animals.remove("tiger")
print(animals)

# sort() # will not work with numbers
animals.sort()
print(animals)

# reverse()
flowers = ["lily","jasmine","rose","goldmarry"]
print(flowers)
flowers.reverse()
print(flowers)

# copy() --- memory are different
flowersB = flowers.copy()
flowersB.append("lotus")
print(flowersB)
print(flowers)

#insert()
flowersB.insert(2,'whiterose')
print(flowersB)

del flowersB
print(flowersB)   





































