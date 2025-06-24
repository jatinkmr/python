# Inheritance
class Car:
    @staticmethod
    def start():
        print('Car Started...')

    @staticmethod
    def stop():
        print('Car Stopped!!')

# For inheriting any class into current class just pass the className inside Paranthesis while declaring new Class
# # Single Level Inheritence
# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# print('car1 Name -> ', car1.name)
# print('car1 Starting...')
# car1.start()

# print('car2 Name -> ', car2.name)
# print("car2 Starting...")
# car2.start()

# print('car2 Stoping...')
# car2.stop()

# print('car1 stoping...')
# car1.stop()

# # Multi-Level Inheritence
# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner('Diesel')
# car1.start()

# Multiple Inheritence
class A:
    varA = "Class A"

class B:
    varB = "Class B"

class C(A, B):
    varC = "Class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
