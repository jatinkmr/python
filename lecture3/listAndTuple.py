# List
# Array in python will called list - List is a collection which is ordered and changeable. Allows duplicate members.
marks = [94.5, 34.5, 99.4, 43.34, 43]
print(marks)
print(type(marks))
print(marks[3])
print(len(marks))

# In python list there is no rule to store the elements of same data-types. We can store mixed data-type values in list
student = ["Karan", 95, 20, "Delhi"]
print(student)

# In python list are mutable(changeable) whereas strings & Tuples are immutable(unChangeable)
student[1] = 82.4
print(student)

print(marks[1:4])
print(marks[-3:-1])

marks.append(45)  # Adds an element at the end of the list
print("marks after appending 45 -> ", marks)

marks.insert(1, 654)
print("marks after inserting 654 at 1 index -> ", marks)

marks.extend(
    [55, 11, 22, 44, 77]
)  # Add the elements of a list (or any iterable), to the end of the current list
print("marks after extending new array -> ", marks)

print(
    "count appearances of 11 -> ", marks.count(11)
)  # Returns the number of elements with the specified value

marks.remove(11)  # remove provided element i.e., 11
print("marks after removing 11 new array -> ", marks)

marks.pop(
    1
)  # remove provided index element. If we don't provide any index then it'll pop last index element automatically
print("marks after poping 1st index -> ", marks)

del marks[2]  # The del keyword also removes the specified index
print("marks after del 2nd index -> ", marks)

marks.extend([55, 11, 22, 44, 77])

marks.sort()
print("marks after sorting -> ", marks)

marks.sort(reverse=True)
print("marks after sorting -> ", marks)

marks.clear()  # clear will remove all elements from the list
print("marks after clearing -> ", marks)

# Tuples
myTuple = ("cherry", "apple", "banana", "cherry")
print(myTuple)
print(myTuple[0])

# For creating a tuple with single value we must have to provide "," always
thistuple = ("apple",)
print(type(thistuple))

# In case we didn't pass "," while creating a tuple it may considered them as int, str, or float which ever data we're using to create tuple
thistuple = "apple"
print(type(thistuple))

print(myTuple.index("apple"))
print(myTuple.count("cherry"))

# fruits = ('apple', 'banana', 'cherry')
# (x, *y) = fruits #"*" may take the rest value from the tuples as per that 'x' takes 'apple' and 'y' take rest 'banana' & 'cherry'
# print(y)

fruits = ("apple", "banana", "cherry", "mango")
(x, *y, z) = fruits
print(y)
