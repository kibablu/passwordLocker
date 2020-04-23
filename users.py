#!/usr/bin/env python3
class User():
    def __init__(self, firstName, lastName, email, password, userName): # special method
        self.firstName = firstName
        self.lastName = lastName    # attributes
        self.email = email
        self.password = password
        self.userName = userName

    def describeUser(self): # method
        print(self.firstName.title() + " is your first name")
        print(self.lastName.title() + " is your last name")
        print(self.email + " is your email")
        print(self.password + " is your password")
        print(self.userName + " is your user name\n")

    def greetUser(self):
        print(self.userName + " Hello, and welcome lovely human\n")

one = User("Alphonso", "Philip", "example@gmail.com", "Alp123", "Alp") # instance of a class User
two = User("Alexis", "sanchez", "alex@gmail.com", "alex123", "alexisofficial")

print("Hello " + one.firstName.title() + "\t" + one.lastName.title() + ".\n") # calling attributes
one.describeUser() # calling method describeUser
one.greetUser()

two.describeUser()
two.greetUser()