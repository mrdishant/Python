file =open("practice.py","r")


ifCount=0
for line in file.readlines():
    if line.__contains__("if"):
        ifCount+=1

print("If count is ",ifCount)        