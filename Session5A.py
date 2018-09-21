# Object and Class
# Object is a Multi Value Container which can store data of your choice
# Data is stored in Key Value Pair, Key is also known as attribute

class User:
    pass

# Object Construction Statement
# u1 is a Ref pointing to Object of User
u1 = User()

# Write Operation
u1.name = "Jennie"
u1.age = 30
u1.phone = "+91 987987987"


# u2 is a Ref Var which points to the object of Dictionary
u2 = {"name":"John","age":30,"phone":"+91 9090909090"}

u3 = User()
u3.uid = 101
u3.name = "Sia"
u3.address = "Redwood Shores"

u4 = u1 # Reference Copy

u4.address = "Redwood Shores"

print(u1)
print(hex(id(u1)))
print(">>>>>>><<<<<<<<")
print(u2)
print(hex(id(u2)))
print(">>>>>>><<<<<<<<")
print(u3)
print(hex(id(u3)))
print(">>>>>>><<<<<<<<")
print(u4)
print(hex(id(u4)))


# Read Operation
print(u4.name,u4.age,u1.phone,u1.address)

# Update Data in Object
u1.name = "Jennie Watson"
u4.age = 37

print(u4.name,u4.age,u1.phone,u1.address)

# Delete Data in Object
# del u1.name
# print(u4.name,u4.age,u1.phone,u1.address) # error

# Delete entire object
# del u1
# print(u4.name,u4.age,u1.phone,u1.address) # error

print(u1.__dict__)
print(u3.__dict__)
print(u4.__dict__)

#Read Operation Formatted
print(u1.name," can be called at ",u1.phone)
print("{} can be called at {}".format(u1.name,u1.phone))