class Counter:

    # Property of Class : Attribute of Class
    myCount = 0

    # Constructor : Property of Class
    def __init__(self):
        self.count = 0

    # Method or Function or Procedure : Property of Class
    def incrementCount(self):
        Counter.myCount = Counter.myCount + 1
        self.count = self.count + 1

    # Method or Function or Procedure : Property of Class
    def showCount(self):
        print("count is",self.count)
        print("myCount is", Counter.myCount)

c1 = Counter()
c2 = Counter()
c3 = c1 # Ref Copy

c1.incrementCount() # -> Counter.incrementCount(c1)
c2.incrementCount()
c3.incrementCount()
Counter.incrementCount(c3)

c1.showCount()
Counter.showCount(c2)
c3.showCount()

# 1,1 | 1,2 | 2,3
# 1,3 | 1,3 | 1,3
# 3,4 | 1,4 | 3,4
# ? | ? | ?
# ? | ? | ?
# ? | ? | ?
# ? | ? | ?
# 1,1 | 1,2 | 2,3

#Program : WhatsAppGroupTitle Object
