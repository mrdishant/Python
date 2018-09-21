a = 100
b = 20
c = 30

#Regular if/else
if a>b:
    print("a is greatest")
else:
    print("b is greatest")

print("************")

# Nesetd if/else
if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
else:
    if b>c:
        print("b is greatest")
    else:
        print("c is greatest")

print("************")

#Ladder if/else
uberGo = 1
uberX = 2
uberMoto = 3

userChoice = uberGo

if userChoice == uberGo:
    print("UberGo Booked !! Cab Arriving Soon !!")
elif userChoice == uberX:
    print("UberX Booked !! Cab Arriving Soon !!")
else:
    print("UberMoto Booked !! Cab Arriving Soon !!")

print("************")
# Short Hand
gpsEnabled = True
# if gpsEnabled:
#     print("You can Browse Google Maps !!")

if gpsEnabled: print("You can Browse Google Maps !!")

print("************")

internetTech = 1
print("Speed Should be greater than 4mbps") if internetTech >=2 else print("You cannot access App !!")

print("************")

# if a>b or a>c:

if a>b and a>c:
    print("a is greatest")

print("########################")

#Loops: while and for !! thats it !
num = 5
i = 1

"""
print(num,i,"'s are",(num*i))
i = i+1
print(num,i,"'s are",(num*i))
i = i+1
print(num,i,"'s are",(num*i))
i = i+1
print(num,i,"'s are",(num*i))
i = i+1
print(num,i,"'s are",(num*i))
i = i+1
print(num,i,"'s are",(num*i))
i = i+1
print(num,i,"'s are",(num*i))
i = i+1
print(num,i,"'s are",(num*i))
i = i+1
print(num,i,"'s are",(num*i))
i = i+1
print(num,i,"'s are",(num*i))
"""

while i<=10:
    print(num, i, "'s are", (num * i))
    i = i+1

print(">>>>>>>>><<<<<<<<<<")

num = 7
for i in range(1,11):
    print(num, i, "'s are", (num * i))

print(list(range(1,101)))

list1 = [10,20,30,40,50]

#ForEach or Enhanced For Loop
for x in list1:
    print(x)


#HW: break and continue

# Problem: in a list of first 100 numbers
# Print the numbers whose binary starts and ends in 1 and starts and ends in 0















