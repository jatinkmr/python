# Class and Object
#  Syntax to create a class:
# class className: -> -> className must be start with Capital Letter
#     <property1>: <Value>
# Syntax to create an object:
# objectName = className()


# class Car:
#     def __init__(self):
#         print("DEFAULT Constructor Called!!")

#     brand = "Ford"
#     color = "Black"
#     tyre = "Aloy Wheel"


# car1 = Car()
# print("brand -> ", car1.brand)
# print("color -> ", car1.color)
# print("tyre -> ", car1.tyre)


# class Person:
#     def __init__(self, name=None, age=None):
#         if name is None and age is None:
#             print("DEFAULT Constructor Called!!")
#             self.name = "DEFAULT NAME"
#             self.age = "DEFAULT AGE"
#         else:
#             self.name = name
#             self.age = age
#         print()
#         self.name = name
#         self.age = age

#     def hello(self):
#         print("hello ", self.name)


# p1 = Person("John", 36)

# print("p1 Object of Person class -> -> ", "p1 name -> ", p1.name, " p1 age -> ", p1.age)
# print(p1.hello())

# p2 = Person()
# print("p2 Object of Person class -> -> ", "p2 name -> ", p2.name, " p2 age -> ", p2.age)
# print(p2.hello())


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def calculateAverageMarks(self):
#         sum = 0
#         for mark in self.marks:
#             sum += mark

#         avg = sum / len(self.marks)
#         return avg


# s1 = Student("Jatin", [25, 45, 67, 45, 23])
# print(f"Hello {s1.name}! Your average marks is {s1.calculateAverageMarks()}!!")


class Account:
    def __init__(self, balance, accountNumber, accountPassword):
        self.balance = balance
        self.accountNumber = accountNumber
        self.__accountPassword = accountPassword  # For declaring the private attribute we may add "__" in front of any self variable. That private attribute can only access inside the class not outside the class

    def debit(self, amount):
        self.balance -= amount
        print(
            f"Your account has been debited with Rs. {amount}. Total Amount in your account is {self.getBalance()}!!"
        )

    def credit(self, amount):
        self.balance += amount
        print(
            f"Your account has been credited with Rs. {amount}. Total Amount in your account is {self.getBalance()}!!"
        )

    def getBalance(self):
        return self.balance

    def resetPass(self):
        print(f"Your password is {self.__accountPassword}")


accountHolder1 = Account(100000, 25041996, "PassWord")
print(f"Your Account Number is {accountHolder1.accountNumber}")
# print(f"Your password is {accountHolder1.__accountPassword}") # that line will throw an error as accountPassword is private due to which it's unable to access outside the class
accountHolder1.debit(45000)
accountHolder1.credit(80000)
accountHolder1.getBalance()
print(accountHolder1.resetPass())
