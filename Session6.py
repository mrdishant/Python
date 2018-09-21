# Single Value Container
a = 10

# Multi Value Container
b = 10,20,30,40,50
c = b # Reference Copy

print(type(a))
print(type(b))

# Multi Value Container - The way we want !!
# Customized Multi Value Container
class Product:
    pass

# Object
# Multi Value Container : Contain Data as Key Value Pair
# Key is also known as Attribute
p1 = Product()

# a, b and p1 are not containing values !!
# They are containing Addresses !! -> Reference Variables

print(a)
print(hex(id(a)))
print(b)
print((c))
print(hex(id(b)))
print(hex(id(c)))
print(p1)
print(hex(id(p1)))

# Writing Data in Object
p1.pid = 101
p1.price = 1000
p1.name = "Sandisk Pen Drive"
p1.color = "Red"
p1.weight = "10 grams"

p2 = Product()
p2.pid = 201
p2.name = "iPhone"
p2.company = "Apple"
p2.warranty = "1 Year"
p2.price = 50000

print(p2)
print(hex(id(p2)))

print("***************")
print(p1.__dict__)
print(p2.__dict__)