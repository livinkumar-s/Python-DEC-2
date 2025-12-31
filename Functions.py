# def printSteps():
#     print("Starting!")
#     print("Running")
#     print("Stopping!")

# printSteps()

# print(123)

# def add(n1,n2):
#     print(n1+n2)

# add(45,54)
# add(45,-54)

# def printVal(a,b):
#     print("Value of A: "+str(a))
#     print("Value of B: "+str(b))
# printVal(5,6)
# printVal(b=45,a=54)


# def printVal(a,b=34):
#     print("Value of A: "+str(a))
#     print("Value of B: "+str(b))

# printVal(5,6)
# printVal(b=45,a=54)

# printVal(2,4)


# print(sum([123,2,23,43]))

# def sumNum(*a):
#     print(sum(a))

# sumNum(9,9,9,4,5,3,54,43,3,2,43,2,43,231)

def collectData(**a):
    print(a)

collectData(name="hendry",age=45,isMarried=True)