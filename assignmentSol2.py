listCD=[]

def sortByIndex(index):
    for i in range(0,len(listCD)):
        for j in range(0,len(listCD)-i-1):
            if(listCD[j][index]>listCD[j+1][index]):
                temp=listCD[j][index]
                listCD[j][index]=listCD[j+1][index]
                listCD[j+1][index]=temp

def createDatabase():
    f=open("CD_Store.txt","r+")
    for f1 in f.readlines():
        try:
            price=float(f1.split(",")[3])
        except Exception as e:
            print("Error in price ",e)
            pass
        listCD.append([f1.split(",")[0],f1.split(",")[1],f1.split(",")[2],price])

def printList():
    for cd in listCD:
        print(cd,"\n")

def findByTitle(target):
    for cd in listCD:
        if(target.lower() in cd[0].lower()):
            print(cd)

def findByGenre(target):

    for cd in listCD:
        if(target.lower() in cd[2].lower()):
            print(cd)

def findByArtist(target):
    
    for cd in listCD:
        if(target.lower() in cd[1].lower()):
            print(cd) 

def findByPrice(targetPrice):
    for cd in listCD:
        if(cd[3]<=targetPrice):
            print(cd)

def main():
    
    createDatabase()

    while(True):
        print("\nPlease Choose from below \n" )

        print("1 to Print List of CDs")

        print("2 to Sort CDs by Title")

        print("3 for Sort CDs by Artist")

        print("4 for Sort CDs by Genre")

        print("5 for Sort CDs by Price")

        print("6 for Find All CDs by Title")

        print("7 for Find All CDs by Artist")

        print("8 for Find All CDs by Genre")
        
        print("9 for Find All CDs with Price at Most X")
        
        print('quit to quit\n')


        i=input()

        if(i=='1'):
            printList()
        elif (i=='2'):
            sortByIndex(0)
        elif (i=='3'):
            sortByIndex(1)
        elif (i=='4'):
            sortByIndex(2)
        elif (i=='5'):
            sortByIndex(3)
        elif (i=='6'):
            findByTitle(input("Enter CD Title : "))
        elif (i=='7'):
            findByArtist(input("Enter Artist name : "))
        elif (i=='8'):
            findByGenre(input("Enter Genre : "))
        elif (i=='9'):
            findByPrice(float(input("Enter target Price : ")))
        elif (i.lower()=='quit'):
            break

main()