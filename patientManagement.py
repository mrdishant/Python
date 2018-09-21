class Patient:


    def __init__(self,):
        self.name=None
        self.age=None
        self.gender=None


    def showDetails(self):
        print("=Patient Details=")
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Gender : ",self.gender)


class PMSystem:

    patients=list()

    def addPatient(self):
        p1=Patient()

        p1.name=input("Enter Patients Name : ")

        p1.age=int(input("Enter Age : "))

        p1.gender=int(input("Specify Gender 0 for Male 1 for Female : "))

        self.patients.append(p1)

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

        i=input();

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
