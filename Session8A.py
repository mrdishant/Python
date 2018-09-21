# 1 Employee Many Projects
# 1 Student Many Assignments
# 1 Teacher Many Students
# 1 College Many Teachers
# Or Any of your choice !!


class Student:

    #Constructor
    def __init__(self, roll, name, age, email, phone):
        self.rollNumber = roll
        self.fullName = name
        self.age = age
        self.email = email
        self.phoneNumber = phone

    #Function or Method
    def showStudentDetails(self):
        print("Student Details",self.rollNumber,self.fullName,self.age,self.email,self.phoneNumber)


s1 = Student(1,"John",21,"john@example.com","+91 9999988888")
s2 = Student(2, "Fionna", 22, "fionna@example.com", "+91 7777788888")
s3 = Student(3, "Sia", 21, "sia@example.com", "+91 9999977777")


# students is a Reference Variable which holds the address of the List
students = [s1,s2,s3]

print(hex(id(students)))

# Printing Reference Variables
print(s1)
print(s2)
print(s3)

######################

class Teacher:

    #Constructor
    def __init__(self, name, experience, qualification, students):
        self.name = name
        self.experience = experience
        self.qualification = qualification
        self.students = students

    def showTeacherDetails(self):
        pass

    def showStudents(self):
        pass

t1 = Teacher("George",5,"MS",students)
t1.showTeacherDetails()
t1.showStudents()

# for stu in t1.students:
#     stu.showStudentDetails()