# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Create class
class User:
#Constructor
def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


def has_birthday(self):
    self.age += 1


# Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance




# Init user object
colson = User('Colson Crim', 'colson@gmail.com', 26)

#Init Customer
janet = Customer('Janet Johnson', 'Janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())


colson.has_birthday()
print(colson.greeting())
