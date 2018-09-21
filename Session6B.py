class Student:

    # Property of Class
    college = "GNE"

    # Constructor
    def __init__(self):
        pass

    # self -> Reference to the Object
    def __init__(self, roll, name, email):
        self.roll = roll
        self.name = name
        self.email = email

# s1 = Student() # Error
s1 = Student(101,"John","john@example.com")
print(s1.__dict__)
print(Student.__dict__)

Student.__init__(s1,201,"Jennie","jennie@example.com")
print(s1.__dict__)