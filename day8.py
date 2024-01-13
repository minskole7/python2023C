# user defined data type 

class Person:
    firstName = 'chinmay'
    lastName = 'deshpande'
    age = 34
    rollNo = 45

    def walk(self):
        print("walks slowly")
    
    def talk(self):
        print("talks rapidly")

# instance of Person
amol =  Person()
print(amol.firstName)
print(amol.lastName)
print(amol.age)
print(amol.rollNo)
amol.walk()
amol.talk()

amol.firstName = "amol"
amol.lastName = "rao"
amol.age = 12
amol.rollNo = 77

# Instance of Person
chinmay = Person()
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.age)
print(chinmay.rollNo)
chinmay.walk()
chinmay.talk()

# Updaing and priting the properties
print(amol.firstName)
print(amol.lastName)
print(amol.age)
print(amol.rollNo)

# program 2
class PersonB:
    # constructor are used to set the properties at the time of object creation
    def __init__(self,fn,ln,ag,rn):
        self.firstName = fn 
        self.lastName = ln 
        self.age  = ag
        self.rollNo = rn

    def walk(self):
        print('I am walking')
    def talk(self):
        print('I am talking')

chinmay = PersonB("chinmay1","deshpande1",34,55)
amol = PersonB("amol1","rao1",33,55)

print(chinmay.firstName)
print(amol.firstName)
chinmay.firstName  = "chinmay"

# program 3 
class Bank:
    def __init__(self,fn,bal):
        self.fullName = fn
        self.balance = bal
        self.transaction = []

    def withdrawl(self,amt):
        if(self.balance > amt):
            self.balance = self.balance - amt
            self.transaction.append(-amt)
            return self.balance
        else:
            print('Insufficient balance')

    def deposit(self,amt):
        self.balance = self.balance + amt
        self.transaction.append(amt)
        return self.balance 
    
    def lastThreeTransation(self):
        print(self.transaction[-3:])

chinmay = Bank("chinmay deshpande",1000)
chinmay.withdrawl(500)
chinmay.deposit(10000)
chinmay.deposit(10000)
chinmay.deposit(10000)
chinmay.deposit(10000)
chinmay.deposit(10000)
chinmay.withdrawl(500)
chinmay.lastThreeTransation()
















