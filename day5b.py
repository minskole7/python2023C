# tuple

listA = [11,22,33,44]
listA[0] = 222
print(listA)
listA.append(4444)
print(listA)


tupleA = (11,22,33,44,55,66,55)
print(tupleA)
print(type(tupleA))
#tupleA[0] = 444444
print(tupleA[0])

#         0  1  2   3  4  5  6
tupleA = (11,22,33,44,55,66,55)

# for loop 
for item in tupleA:
    print(item)
print(44 in tupleA)

# for loop with range
for item in range(len(tupleA)):
    #print(item)
    print(tupleA[item])

# while loop
h1 = 0
while(h1 < len(tupleA)):
    #print(h1)
    print(tupleA[h1])
    h1 = h1 + 1

#         0  1   2  3 4
tupleB = (22,33,44,55,33)
h2 = tupleB.count(33)
print(h2)

k = tupleB.index(55)
print(k)






