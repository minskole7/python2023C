#set
# string , list , dictionary , set ,tuple
setA = {11,22,33,44,55,22,33,44,55}
print(setA)

# set stores the value by index ??
#print(setA[0])
# looping over set
for item in setA:
    print(item)


cities = {"nagpur","chandrapur","banglore","kolkata","chennai"}
print(cities)
print(type(cities))
print(len(cities))


# add()
setB = {11,22,33,44}
setB.add(55)
print(setB)

# remove
setB.remove(33)
print(setB)

# pop()
setB.pop()
print(setB)

#clear()
setB.clear()
print(setB)

setC = {"chinmay","sarika","poorva"}
setC.update(["chinmay","mayuri","ram"])
print(setC)


# program 1
setD = {11,22,33}
setE = {22,33,44}
setF = setD.intersection(setE)
print(setF)

setD.intersection_update(setE)
print(setD)

# program 2

setD = {11,22,33}
setE = {22,33,44}

f = setE.difference(setD)
print(f)
setE.difference_update(setD)
print(setE)

# program 4
setD = {11,22,33}
setE = {22,33,44}
setF = setD.union(setE)
print(setF)

# program 5
setD = {11,22,33}
setE = {22,33,44}

setQ = setD.symmetric_difference(setE)
print(setQ)

setD.symmetric_difference_update(setE)
print(setD)

# program 6
setD = {11,222,333}
setE = {22,33,44}
setB  = setD.isdisjoint(setE)
print(setB)

# program 7
setD = {11,22,33}
setE = {11,22}
w = setD.issuperset(setE)
print(w)

t = setE.issubset(setD)
print(t)

# program 8
setD = {11,22,33}
print("hello")
print(setD.discard(44))
print("bye")
#setD.remove(44)


















