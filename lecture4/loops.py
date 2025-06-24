# WHILE Loop
count1 = 1
while count1 < 101:
    print("count1 -> ", count1)
    count1 += 1

count2 = 100
while count2 > 0:
    print("count2 -> ", count2)
    count2 -= 1

num = int(input('Enter any number for table...'))
i = 1
while i < 11:
    print(num, " X ", i, " = ", num * i)
    i += 1;

arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
indx = 0
while indx<len(arr):
    print('element at ', indx, ' index -> ', arr[indx])
    indx += 1;

indx1 = 0
while indx1<len(arr):
    print('index -> ', indx1)
    if (arr[indx1] == 25):
        print('25 found at', indx1, 'index!!')
        break;

    indx1 += 1;

# FOR Loop
for index, num in enumerate(arr):
    print(f'index -> {index}, num -> {num}')

# range(start, stop, step), range(start, stop), range(stop)
for num6 in range(1, 5, 2):
    print(f"num -> {num6}")

for num5 in range(1, 5):
    print(f"num -> {num5}")

for num4 in range(5):
    print(f"num -> {num4}")

num3 = int(input("Enter any number for table..."))
for n in range(1, 11):
    print(f"{n} X {num3} = {num3*n}")

sum = 0
num1 = int(input("Enter n number to find the sum of those n numbers..."))
for n in range(1, num1 + 1):
    print("sum -> ", sum, "num -> ", n)
    sum += n
    print("sum -> ", sum)

print(f"sum of {num1} numbers are {sum}")


fact = 1;
num = int(input("Enter n number to find the factorial of n numbers..."))
for n in range(1, num+1):
    fact *= n;

print(f"Factorial of {n} numbers are {fact}");
