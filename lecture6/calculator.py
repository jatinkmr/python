class Calculator:
    def __init__(self, num):
        self.num = num

    def showNumber(self):
        return self.num

    def add(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def div(self, other):
        return self.num / other.num


num1 = Calculator(1)
num2 = Calculator(2)

print(f"num1 -> {num1.showNumber()}")
print(f"num2 -> {num2.showNumber()}")

sum = num1.add(num2)
print(f"sum -> {sum}")

sub = num1 - num2
print(f"sub -> {sub}")

mul = num1 * num2
print(f"mul -> {mul}")

div = num1.div(num2)
print(f"div -> {div}")