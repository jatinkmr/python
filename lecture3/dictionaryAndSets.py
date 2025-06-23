# Dictionary - Dictionaries are used to store data values in key:value pairs just like an object. A dictionary is a collection which is ordered*, changeable and do not allow duplicate keys.
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"],
    "dimensions": {"height": 40, "weight": 90, "length": 120},
}
print(thisDict)
print("len -> ", len(thisDict))
print("typeOf -> ", type(thisDict))
print("brand -> ", thisDict["brand"])
print("model -> ", thisDict["model"])
print("year -> ", thisDict["year"])
print("height -> ", thisDict["dimensions"]["height"])
print("weight -> ", thisDict["dimensions"]["weight"])
print("length -> ", thisDict["dimensions"]["length"])
print("keys -> ", thisDict.keys())
print("values -> ", thisDict.values())
print("items -> ", thisDict.items())
print("get -> ", thisDict.get("brand"))

thisDict["type"] = "4-vehicle"  # Adding new element
thisDict["colors"].append("black")  # Updating the existing value
thisDict.update({"year": 1965})  # To update the value of particular key

print(thisDict)

thisDict.clear()  # Clearing the dictionary
print(thisDict)

# Sets - Sets are used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable*, and unindexed.Sets are written with curly brackets.
# Set items are unordered, unchangeable(im-mutable), and do not allow duplicate values(unique). List and Dict cannot be stores into Set as we can change/update their values.
# Set are mutable but elements are im-mutable. Set are exactly same as Mathematics Set.
set1 = {1, 2, 3, 4}
print('set1 -> ', set1)
set2 = {1, 2, 2, 2}  # Repeated elements stored only once. So, it may resolved to {1, 2}
print('set2 -> ', set2)
print('length -> ', len(set2))
set3 = set() # To declare an empty set we may use set function
print('set3 -> ', set3)

print('set1 Type -> ', type(set1))


print('Set methods -> -> -> ')
set1.add(3)
set1.add(5)
print("After updating set1 -> ", set1)

print('Difference between set1 and set2 -> ', set1.difference(set2)) # Find the difference between 2 sets

print('set1 -> ', set1)
print("set2 -> ", set2)
set1.difference_update(set2) # Find and update the set as per the difference
print("After different_update")
print("set1 -> ", set1)
print("set2 -> ", set2)

fruitsDiscard = {"apple", "banana", "cherry"}
fruitsDiscard.discard("banana")
print(fruitsDiscard)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print('Difference between x and y -> ', x.intersection(y)) # Find the common element
x.intersection_update(y)
print('x after intersection_update -> ', x)

