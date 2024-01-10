# python 
# variables 
# arithmetic operator 
# comparison operator 
# logical operator 
# conditional statement 
# loops 
# list 
# dictionary 
# str

# program 1
first_name = "chinmay"
last_name = 'deshpande'

info = """
    This is minskole and 
    i learning python over here
"""

info2 = ''' 
    This is minskole and 
    i am learning java over here
'''

print(first_name)
print(type(first_name))
print(type(info2))

# string stores the value by index
city = "pune"
#0     1     2    3
#p     u     n    e
print(city[0])
print(city[1])
print(city[2])
print(city[3])

# program 2  # loop over a string 

city = "chandrapur"

# 0   1   2  3  4  5  6  7  8  9
# c   h   a  n  d  r  a  p  u  r

# for with range function
for ch in range(10):
    print(city[ch])

# for without range 
for ch in city:
    print(ch)

# while loop
i = 0
while(i < len(city)):
    #print(i)
    print(city[i])
    i = i + 1


cities = ["pune","mumbai","banglore","kolkata"]
print(cities)
print(cities[0])
cities[0] = "nagpur"
print(cities)

city2  = "goa"
print(city2[0])
#city2[0] = "b"

# program 3
first_name = "chinmay"
q1 = first_name.upper()
print(q1)

last_name = "deshpande"
q2 = last_name.lower()
print(q2)

# program 4
city = "chandrapur"
# 0  1  2  3  4  5  6   7  8   9
# c  h  a  n  d  r  a   p  u   r
#-10-9 -8 -7 -6 -5 -4  -3 -2  -1
#string[startIndex:endIndex(not included:stepSize)]
print(city[0:])
print(city[1:7])
print(city[-9:8])
print(city[-9:-1])
print(city[-5:])
print(city[-1:-9])
print(city[-1:0])

# program 5
# 0 1 2 3 4 5
# j a i p u r 

# startswith()
city = "jaipur"
print(city.startswith("j"))
print(city.startswith("jai"))

# endswith()
print(city.endswith("r"))
print(city.endswith('pur'))

# index()
print(city.index('a'))

# program 6
city = "jaipur "
city1 = " jaipur"
city2 = " jaipur "

print(len(city))
print(len(city1))
print(len(city2))

print(len(city.rstrip()))
print(len(city1.lstrip()))
print(len(city2.strip()))


# program 7

strA = "abc"
print(strA.isalpha())

strB = "12323435345"
print(strB.isdigit())

strC = "12323435345"
strC = "aa"
strC = "a23324"
strC = "#asdsad"

print(strC.isalnum())

# program 8
info = 'i am learning javascript'
info = info.replace('javascript','python')
print(info)


# program 9 
info = "I am learning javascript"
a = info.split(" ")
b = info.split("a")
print(a)
print(b)

#["I","am","learning","javascript"]
#info = ["I ","m le,","rning j","v","script"]


city = "nagpur"
cu = city.upper()
cua = city.capitalize()
print(cu)
print(cua)
#"chinmaydeshpande@gmail.com".split('#')[0]


























