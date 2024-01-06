#          0          1        2  3
info = ["chinmay","deshpande",12,23]

# retrive
print(info[0])
# update
info[0] = "tanmay"
print(info)
# add
info.append('pune')
print(info)
# delete
info.pop()
print(info)

# info = ["chinmay","deshpande",12,23]

info = {
    # property:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age": 23,
    "rollNo":12
}
# Retrive
print(info['firstName'])
# Update
info['lastName'] = "Dani"
print(info)
# Add
info['city'] = "pune"
print(info)
# Delete
info.pop('firstName')
print(info)

# program 2

vehicle = {
    "color":"red",
    "type":"sedane"
}
print(vehicle)
print(type(vehicle))

# retrive
print(vehicle['color'])
# add
vehicle['regNo'] = 123
#update
vehicle['type'] = "SUV"
#delete
vehicle.pop('type')

# Can we store duplicate keys in dict
animals = {
    "color":"red",
    "legs":4,
    "color":"blue"
}
print(animals)

info2 = {
    "fn":"chinmay",
    "ln":"deshpande",
    "age":13,
    "rollNo":45
}

# pop() , popitem()
# info2.pop('fn')
# info2.popitem()
# print(info2)

#clear()
# info2.clear()
# print(info2)

#get()
a = info2.get('ln')
b = info2['ln']
print(a)
print(b)

# loop through dictionary

info2 = {
    "fn":"chinmay",
    "ln":"deshpande",
    "age":13,
    "rollNo":45
}

for key in info2:
    print(key)

print('fn' in info2)
print(len(info2))


info2.update({"language":"hindi","city":"pune"})
print(info2)

info2 = {
    "fn":"chinmay",
    "ln":"deshpande",
    "age":13,
    "rollNo":45
}

for key in info2.keys():
    print(key)

for val in info2.values():
    print(val)

for k,v in info2.items():
    print(k,v)


info3 = info2.copy()
info3['district'] = "pune area"
print(info3)
print(info2)

q1 = dict.fromkeys(["a","b","c"],0)
print(q1)


info2 = {
    "fn":"chinmay",
    "ln":"deshpande",
    "age":13,
    "rollNo":45
}

q2 = info2.setdefault('city',"pune")
print(q2)
print(info2)