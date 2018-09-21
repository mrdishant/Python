# One to Many Relationship

# Review of List
names = ["John","Jennie","Jim"]
print(names)
print(type(names))

names.append("Jack")

print(names)

print(names[3])

for name in names:
    print(name)


class Address:

    #Constructor
    def __init__(self, adrsLine, city, state, zipCode):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state
        self.zipCode = zipCode

    def showAddress(self):
        print("Address Details: ",self.adrsLine,self.city,self.state,self.zipCode)


a1 = Address("Pristine Mangnum","Bengaluru","Karnataka",520001)
a2 = Address("Country Homes","Ludhiana","Punjab",141002)

print(a1)
print(a2)

# a1.showAddress()
# a2.showAddress()

# Multi Value Container adrsList is a collection of Multi Value Containers i.e. Objects
adrsList = [a1, a2]
print(adrsList)

adrsList[0].showAddress()
adrsList[1].showAddress()

# Create a Code Snippet : Employee works on Many Projects