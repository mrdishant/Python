#Variable Arguments : Tuple (*args)
# def fun(*john):
def fun(*args):
    print(args)
    print(type(args))

    print("**********")
    for x in args:
        print(x)
    print("**********")


fun(10,20,30)
fun(10,20,30,40,50)
fun("John","Jennie","Jim","Jack","Joe")
fun("John")
fun(10)
fun()

list1 = [10,20,30]
list2 = ["John","Jennie","Jim"]
fun(list1)
fun(list1,list2) # Tuple of Lists

print("===============")

#Variable Arguments : Dictionary (**kwargs)
def funAgain(**kwargs):
    print(kwargs)
    print(type(kwargs))

funAgain(a=10,b=20,c=30)
funAgain(allNums=list1, allNames=list2, x=10)

# data1 = {101:"John",201:"Jennie"}
# data2 = {"allNums":[10,20,30,40,50],201:"Jennie"}
