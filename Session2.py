# Single Value Containers
a = 10
b = 20
c = a+b

print("a is",a)
print("b is",b)
print("c is",c)

print("type of a is",type(a))
print("type of b is",type(b))
print("type of c is",type(c))

d = 2.2
print("d is",d)
print("type of d is",type(d))

char = 'A'
name = 'John Watson'

print("char is",char)
print("name is",name)

print("type of char is",type(char))
print("type of name is",type(name))

businessName1 = 'John\'s Coffe Shop'
businessName2 = "John's Cafeteria"

print("businessName1 is",businessName1)
print("businessName2 is",businessName2)

message = """Search the Candle !!
   Rather than cursing the darkness !! """
print(message)

x = 100
y = x # Address Copy

print("x is",x)
print("y is",y)

print("hex id of x is",hex(id(x)))
print("hex id of y is",hex(id(y)))

flag = True
print(type(flag))

num1 = a + flag
#num2 = a + businessName1 # error
print(num1)
#print(num2)

# STRINGS in Python
# Strings are IMMUTABLE i.e. they cannot be changed
name1 = "Sia Flynn"
name2 = name1.upper()

print("name1 is",name1)
print("name2 is",name2)

print(name1[0])
print(name1[-1])

# Multi Value Container
p = 10,20,30,40,50,30  # Tuple
#p = (10,20,30,40,50)

q = [10,20,30,40,50,30]

print("p is",p)
print("p type is",type(p))

print("q is",q)
print("q type is",type(q))

n1 = 10
print("n1 type is",type(n1))
n1 = (10,20)
print("n1 type is",type(n1))
n1 = "This is Awesome"
print("n1 type is",type(n1))

r = {10,20,30,40,50,30}
print("r is",r)
print("r type is",type(r))

s = {101:"John",201:"Jennie"}
print("s is",s)
print("s type is",type(s))

#Multi Value Container : Container of Containers

#List of Lists
population = [
                [103,456,754,123,987],
                [654,987,777,678,321,456]
             ]
print(population)
print("type of population is",type(population))

# Problem
# Compute Who Won in Elections ?
# PartyA   PartyB

print(population[0])
print(population[1])

print(population[0][0])