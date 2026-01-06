# Creating class 

class Bottle:
    # attributes
    def __init__(self):
        self.radius="50mm"
        self.capacity="1ltr"
    
    # Methods
    def open(self):
        print("Bottle is getting opened...!")
    def close(self):
        print("Bottle is getting closed...!")

#2 attr and 2 methods

class Dog(Bottle):
    def __init__(self):
        self.name="Lucky"
        self.legs=4
    
    def bark(self):
        print("Bow Bow")

# 2 attr and 1 method
# d1=Dog()
# d1.open()

b1=Bottle()
b1.open()

# b1=Bottle()
# d1=Dog()
# d2=Dog()
# d3=Dog()
# d4=Dog()

# print(b1.capacity)
# print(b1.radius)
# b1.open()
# b1.close()

# d1.bark()

# a=1 #new int object from int
# b="Hello world" # created using str
# c=[1,2,3,4,5]



# list # the methods that were defined inside this class can be accessed by the object created using this class

# a=1
# b="String"
# c=Bottle()

# print(type(c)) #<class __main__.'Bottle'>
