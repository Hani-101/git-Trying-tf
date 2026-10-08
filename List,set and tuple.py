# nested loop = A loop inside a loop (outer loop and inner loop)
## outer loop = The loop that contains the inner loop
## inner loop = The loop that is inside the outer loop
#import time

#rows = int(input("Enter the number of rows: "))
#columns = int(input("Enter the number of columns: "))
#symbol = input("Enter the symbol to use: ")

#for x in range(rows):
#    for y in range(columns):
#        print(symbol, end="")
#    print()
#...................................................................................................................

 # collection = single "variable" used to store multiple values.
#  List = [] ordered and changeable. Duplicates allowed
#  Set = {} unordered and immutable, but Add/Remove OK. No duplicates allowed like ["apple", "banana", "apple"] wrong = ["apple", "banana"] right
#  Tuple = () ordered and unchangeable. Duplicates allowed. FASTER "than list"

fruits = ("apple", "banana", "cherry", "coconut","coconut")
#  Tuple = ()
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("MO" in fruits)

#print(fruits.index("apple")) # this will return the index of "apple" in the tuple
print(fruits.count("coconut"))
for fruit in fruits:
    print(fruit)
#....................................................................
#sets {}
#print(len(fruits))
#print("coconut" in fruits)

#fruits.add("Mashroom")
#fruits.remove("banana")
#fruits.clear()
#fruits.pop() # this will remove a random item from the set
#print(fruits)


#.........................................................
# Lasts []
#print(dir(fruits)) # this will print all the methods available for the list "fruits"
#print(help(fruits))
#print(fruits[::-1])
#print(len(fruits))
#print("Kinder" in fruits) # u can use "in" to check if a value exists in a list or not. If it exists, it will return True, if not, it will return False.

#fruits[0] = "kiwi" # this will change the first item in the list to "kiwi"

#fruits.append("orange") # this will add "orange" to the end of the list
#fruits.remove("cherry")
#fruits.insert(0, "date") # this will add "date" to the beginning of the list
#fruits.sort() # this will sort the list in alphabetical order
#fruits.reverse() # this will reverse the order of the list
#fruits.clear() # this will remove all items from the list
#print(fruits.index("apple")) # this will return the index of "apple" in the list
#print(fruits.count("banana")) # this will return the number of times "banana" appears in the list 


#print(fruits)

#print(fruits[0:3]) # this will print the first 3 items in the list
#for fruit in fruits:
#    print(fruit)
