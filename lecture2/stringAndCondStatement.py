# String is a data type that stores a sequence of characters!!
# str1=input('Enter your first string...')
str1='Jatin'
print(f"You've entered: \t {str1} which starts from {str1[0]} and end at {str1[len(str1)-1]} whose length is {len(str1)}");
print('str1[1:3]', str1[1:3])

# In python we can also do backward or negative index which starts with "-1".
print('str1[-3:-1]', str1[-3:-1])

encodeStr = "My name is Jåtǐň"
encodeX = encodeStr.encode()
print(encodeX)

findStr = "Hello, welcome to my world."
findX = findStr.find("welcome")
print(findX)

indexStr = "Hello, welcome to my world."
indexX = indexStr.index("welcome")
print(indexX)

alphaStr = "CompanyX"
alphaX = alphaStr.isalpha()
print(alphaX)

asciStr = "Company123"
asciX = asciStr.isascii()
print(asciX)

isNumericStr = "565543"
isNumericX = isNumericStr.isnumeric()
print(isNumericX)

lStripStr = "     banana     "
lStripX = lStripStr.lstrip()
print("of all fruits", lStripX, "is my favorite")

upperStr = "Hello my friends"
upperX = upperStr.upper()
print(upperX)

# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83: 80};
txt = "Hello Sam!"
print(txt.translate(mydict));

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

#Conditional Statement
light = 'red'

if (light == 'red'):
    print('Stop!!')
elif(light == 'green'):
    print('go')
elif(light == 'yellow'):
    print('look')
else:
    print('in else part')

# num = int(input('Enter any number to check whether it is odd or even...'))
num=6532;
if ((num%2) == 0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")

num1 = int(input('Enter 1st number...'))
num2 = int(input('Enter 2nd number...'))
num3 = int(input('Enter 3rd number...'))

if ((num1>num2) and (num1>num3)):
    print(f"{num1} is greater")
elif(num2>num3):
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

