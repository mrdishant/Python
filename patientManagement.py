class Patient:

    def __init__(self):
        self.name=None
        self.age=None
        self.gender=None


    def showDetails(self):
        print("=Patient Details=")
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Gender : ",self.gender)

    def getPatient(self):
        return  ""+self.name+str(self.age)+str(self.gender)+"\n"   


class PMSystem:

    file=open("patients.txt","r+")      

    patients=list()

    def __init__(self):
        print("hello")
        for line in PMSystem.file.readlines():
            print(line)
            PMSystem.patients.append(line)

    def addPatient(self):
        p1=Patient()

        p1.name=input("Enter Patients Name : ")

        p1.age=int(input("Enter Age : "))

        p1.gender=int(input("Specify Gender 0 for Male 1 for Female : "))

        self.patients.append(p1)

        PMSystem.file.write(str(p1.__dict__)+"\n")

        print("!!! Patient Added Successfully !!!\n")

    def showAll(self):

        for patient in self.patients:
            print("================")
            patient.showDetails()

            print("================\n")

             

    def showAllAgeSort(self):

        sortedList=sorted(self.patients, key=lambda x: x.age)
        for patient in sortedList:

            print("================")
            patient.showDetails()
            print("================\n")

    def showAllGender(self,value):

        for Patient in self.patients:
            if(Patient.gender==value):

                print("================")
                Patient.showDetails()

                print("================\n")      
        

def main():

    pmsystem=PMSystem()

    while(True):
        print("\nPlease Choose from below \n" )

        print("1 to Add Patient")

        print("2 for List of Patients")

        print("3 for List of Patients (Age Sort)")

        print("4 for List of Patients (Male)")

        print("5 for List of Patients (Female)\n")

        i=input()

        if(i=='1'):
            pmsystem.addPatient()
        elif (i=='2'):
            pmsystem.showAll()  
        elif (i=='3'):
            pmsystem.showAllAgeSort()
        elif (i=='4'):
            pmsystem.showAllGender(0)
        elif (i=='5'):
            pmsystem.showAllGender(1)


main()            
# fileName="patients.txt"
# # fileR=open(fileName,"r")

# fileW=open(fileName,"a+")

# # print(fileR.readlines())

# fileW.write("hello")

# # print(fileR.readlines())

