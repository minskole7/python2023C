# # Oops -- inheritance 

# # program 1
# class Student:

#     def __init__(self,fn,ln,age):
#         self.firstName = fn 
#         self.lastName = ln 
#         self.age = age 

#     def displayName(self):
#         print(self.firstName + self.lastName)

# amol = Student("amol","rao",23)
# print(amol.lastName)
# print(amol.firstName)
# print(amol.age)
# amol.displayName()

# program 2

# parent class
class Student:

    def __init__(self,fn,ln,ssn):
        self.firstName = fn 
        self.lastName = ln 
        self.ssn = ssn

    def displayName(self):
        print(self.firstName+ self.lastName)

# child class
class Teacher(Student):
     salary = 1000

     def displaySalary(self):
         print(self.salary)

chinmay = Teacher("chinmay","deshpande",23)
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.ssn)
print(chinmay.salary)
chinmay.displayName()
chinmay.displaySalary()


# single inheritance
class GrandFather:
    # constructor
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayGName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self, fn, ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn

    def displayFName(self):
        print(self.fname+ self.lastName)

shirish = Father("manohar","deshpande","deshpande")
print(shirish.firstName)
print(shirish.lastName)
print(shirish.fname)
shirish.displayGName()
shirish.displayFName()
        
# Multilevel
# A 
class GrandFather:
    # constructor
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayGName(self):
        print(self.firstName + self.lastName)

# B
class Father(GrandFather):
    def __init__(self, fn, ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn

    def displayFName(self):
        print(self.fname+ self.lastName)

# C
class Son(Father):
    def __init__(self, fn, ln, ffn,ssn):
        super().__init__(fn, ln, ffn)
        self.sname = ssn

    def displaySName(self):
        print(self.sname + self.lastName)

chinmay = Son("manohar","deshpande","shirish","chinmay")
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.fname)
print(chinmay.sname)

chinmay.displayGName()
chinmay.displayFName()
chinmay.displaySName()


# Herarchical 

class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayMname(self):
        print(self.firstName+ self.lastName)

class Son(Mother):
    def __init__(self, fn, ln,sname):
        super().__init__(fn, ln)
        self.sname = sname

    def displaySName(self):
        print(self.sname+ self.lastName)


class Daughter(Mother):
     def __init__(self, fn, ln,dname):
        super().__init__(fn, ln)
        self.dname = dname

     def displayDName(self):
        print(self.dname+ self.lastName)

chinmay = Son("kanchan","deshpande","chinmay")
chinmay.displaySName()
chinmay.displayMname()
gauri =  Daughter("kanchan","deshpande","gauri")
gauri.displayDName()
gauri.displayMname()

# Multiple inheritance # two parents and one child 
class Father:
    def __init__(self,fn,ln):
        print("Father constructor called")
        self.firstName = fn 
        self.lastName = ln

    def displayFname(self):
        print(self.firstName+ self.lastName)
class Mother:
    def __init__(self,fn,ln):
        print("Mother constructor")
        self.firstName = fn 
        self.lastName = ln

    def displayMname(self):
        print(self.firstName+ self.lastName)

class Son(Father,Mother):
    def __init__(self, fn, ln,sname):
        super().__init__(fn, ln)
        self.sname = sname 

    def displaySname(self):
        print(self.sname+ self.lastName)

chinmay = Son("shirish","deshpande","chinmay")





















