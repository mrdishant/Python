
class CD:


    def __init__(self,aName,sName,type,price):
        self.aName=aName
        self.sName=sName
        self.type=type
        self.price=price

    def getArtist(self):
        return self.sName

    def getPrice(self):
        return str(self.price)

    def __str__(self):
        return ("{} by {} at {} is of {} Genre".format(self.aName,self.sName,self.getPrice(),self.type))
    def __rep__(self):
        return self.aName
        

class StoreHelper:


    f=open("CD_Store.txt","r+")
    
    listCD=[]

    def __init__(self):
        for f1 in self.f.readlines():
            try:
                price=float(f1.split(",")[3])
            except Exception as e:
                pass

            self.listCD.append(CD(f1.split(",")[0],f1.split(",")[1],f1.split(",")[2],price))
        
    def sortByArtist(self):
        

        sortedList=sorted(self.listCD, key=lambda x: x.sName)

        newFile=open("CD_Store.txt","w+")

        for cd in sortedList:
            print(cd,"\n")
            newFile.write(cd.aName+","+cd.sName+","+cd.type+","+str(cd.price)+"\n")


    def sortByPrice(self):
        
        sortedList=sorted(self.listCD, key=lambda x: x.price)


        newFile=open("CD_Store.txt","w+")

        for cd in sortedList:
            print(cd,"\n")
            newFile.write(cd.aName+","+cd.sName+","+cd.type+","+cd.getPrice()+"\n")

    def searchTitle(self,target):
        for cd in self.listCD:

            if(target.lower() in cd.aName.lower()):
                print(cd)

    def searchGenre(self,target):
    
        for cd in self.listCD:
            if(target.lower() in cd.type.lower()):
                print(cd)

    def searchArtist(self,target):
        
        for cd in self.listCD:
            if(target.lower() in cd.sName.lower()):
                print(cd) 

    def searchPrice(self,targetPrice):
        for cd in self.listCD:
            if(cd.price<=targetPrice):
                print(cd)
            


def main():
    
    storeHelper=StoreHelper()

    while(True):
        print("\nPlease Choose from below \n" )

        print("1 to Sort by Artist")

        print("2 for Sort by Price")

        print("3 for FindByTitle")

        print("4 for FindByGenre")

        print("5 for FindByArtist")

        print("6 for FindByPrice\n")

        print('quit to quit\n')

        i=input()

        if(i=='1'):
            storeHelper.sortByArtist()
        elif (i=='2'):
            storeHelper.sortByPrice()  
        elif (i=='3'):
            storeHelper.searchTitle(input("Enter Taget Title here : "))
        elif (i=='4'):
            storeHelper.searchGenre(input("Enter Taget Genre here : "))
        elif (i=='5'):
            storeHelper.searchArtist(input("Enter Artist name here : "))
        elif (i=='6'):
            storeHelper.searchPrice(float(input("Enter Target price here : ")))
        elif (i.lower()=='quit'):
            break

main()
