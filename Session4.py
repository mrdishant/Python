#Main Thread: Xxecution Context

print(__name__) # __main__ as the name of main thread
a = 10
b = 20
c = a+b
print(c)

for i in range(1,10):
    print(i)

#Function : is a block of statements
#           which will execute the statements one by one

# Definition of a Function
# Function without Inputs
def sayHello():
    print("Welcome !!")
    print("Its an Awesome Day !!")

# Execution of Function or Calling a Function
sayHello()
print("********")
sayHello()

# Function with Inputs
# def addNumbers(x=1, y=1):
def addNumbers(x, y):
    sum = x+y
    print("Addition of",x,"and",y,"is",sum)

addNumbers(100,200)
addNumbers(12,2)
addNumbers(11,13)

# Function with Inputs and Function is acknowledging back in the end
def squareOfNum(num=3):
    square = num*num
    return square # ack, which should always be in the end

sq = squareOfNum(5)
print("square of 5 is",sq)
print("square of 11 is",squareOfNum(11))
print("square of 11.11 is",squareOfNum(11.11))
print("square of number is",squareOfNum())
#print("square of A is",squareOfNum('A')) #error

def canVote(age=10):
    return (age>=18)

print("If Jennie's age is not known?",canVote())
print("If John is 18 years old can he vote?",canVote(18))

