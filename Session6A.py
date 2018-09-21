class User:
    # Property of Class
    uid = "NA"
    age = 0


# Object Construction Statement
u1 = User()

# Writing Data in Object
u1.name = "John Watson"
u1.email = "john@example.com"
u1.password = "john123"

#Updating Data in Object
u1.name = "John Watson W"

# Reading Data from Object
# print(u1.name,"can be emailed at",u1.email)
print("{} can be emailed at {}".format(u1.name,u1.email))

# Reference Copy
u2 = u1
print(u1)
print(u2)

u1.name = "Fionna Flynn"
u1.email = "fionna@example.com"

print("{} can be emailed at {}".format(u2.name,u2.email))

print(u1.__dict__)
print(u2.__dict__)

User.uid = 101
User.age = 30
User.address = "Redwood Shores"

print(User.__dict__)

print(u1.address)

u3 = User()
u3.address = "Pristine Magnum"

print(u3.__dict__)
print(u3.address)

# print(User.email) # Error
