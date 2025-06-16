# Design a class as described below.
# class name : MyClass
# function: function name - display(), parameters - none, return type - void , access modifier - public, function body - should print "Hello World"

class MyClass:
    def display(self):
        print('Hello World')

obj = MyClass()
obj.display()

# Design a class as described below.
# class: User
# instance variable: name(String)
# constructor: parameter: none, task: initialize the instance variable to "Default"

class User:
    def __init__(self):
        self.name="Default"

user = User()
print(user.name)
