#Student
roll1 = 1
name1 = "John"
phone1 = "990099009900"
email1 = "john@example.com"

roll2 = 2
name2 = "Jennie"
phone2 = "880099009900"
email2 = "jennie@example.com"

student1 = {"roll":1,"name":"John","phone":"9090909090","email":"john@example.com"}
student2 = {"roll":2,"name":"Jennie","phone":"8090909090","email":"jennie@example.com"}

print(type(student1))
print(type(student2))

# User Defined Type : class
# Why? Because we wish to have a storage container which is customizable
class Student:

    # Data Read Operation
    def show(self):
        print(self.name,"is",self.age,"years old")

    # Data Processing
    def canVote(self):
        if self.age >= 18:
            print(self.name,"can vote")
        else:
            print(self.name, "cannot vote")



#Object Construction
s1 = Student()
s2 = Student()

s1.roll = 101
s1.name = "John"
s1.age = 30

s2.roll = 201
s2.name = "Jennie"
s2.age = 22

print(student1)
print(student2)

print("************")

print(type(s1))
print(type(s2))

s1.show()
s2.show()

s1.canVote()
s2.canVote()

print(s1)
print(s2)