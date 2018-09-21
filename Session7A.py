class Student:

    #Constrcutor
    def __init__(self, roll, name, age, address):
        self.roll = roll
        self.fullName = name
        self.age = age
        self.address = address


class Address:

    #Constructor
    def __init__(self, adrsLine, city, state, zipCode):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state
        self.zipCode = zipCode

class Company:
    pass

# Lets Create Objects Now !!
c1 = Company()

addressLine = input("Enter Address Line: ")

a1 = Address(addressLine,"Bengaluru","Karnataka",520001)
s1 = Student(101,"John",30,a1)


print(c1)
print(s1)
print(a1)

c1.companyName = "Auribises"
c1.address = "Redwood Shores"

s1.std = 10
a1.landMark = "Sony World"

print("===Company====")
print(c1.__dict__)

print("===Student====")
print(s1.__dict__)

print("===Address====")
print(a1.__dict__)

print(s1.fullName)
print(s1.address) #?
print(s1.address.adrsLine) #?


print("***************")
name = input("Enter Your Name: ")
age = input("Enter Your Age: ")

print("Hello,",name)
print("Your Age is:",age)

