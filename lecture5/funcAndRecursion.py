# Functions
# To make any function we may use "def" Keyword
# Syntax: def <functionName> (arguments):
def factorial(num):
    fact = 1
    for n in range(1, num + 1):
        fact *= n

    return fact


num = int(input("enter any number to find the factorial..."))
print(f"Factorial of {num} is {factorial(num)}")


# Recursion
def recrusiveFactorial(num):
    if num == 1:
        return num
    else:
        return num * recrusiveFactorial(num - 1)

recursiveNum = int(input("enter any number to find the factorial using Recusion..."))
print(f"Factorial of {recursiveNum} is {recrusiveFactorial(recursiveNum)}")

