# example 1
# name = input("What is your name?: ")
# "if name == "": True execute this code 4 ever"
# while name == "":
#     print("You didn't enter a name.")
#     name = input("What is your name?: ")
#
# else:
#     print(f"Hello, {name}!")

# example 2
# age = int(input("What is your age?: "))
# while "age < 18" is true: execute this code 4 ever"
# while age < 18:
#     print("You are not old enough to enter.")
#     age = int(input("What is your age?: "))
#
# print("You are old enough to enter.")

# example 3

#food = input("What is your favorite food?: ")
# while "food != 'q'" is true: execute this code 4 ever - " if u do not enter "q" it will keep asking for your favorite food"
#while food != "q":
#    print(f"{food} is my favorite food too!")
#    food = input("What is your favorite food?: ")

#print("You have exited the program.")    

# example 4

num = int(input("Enter a number between 1 and 10: "))
# while "num < 1" is true or "num > 10"is true: execute this code 4 ever
while num < 1 or num > 10:
    print(f"{num} is not between 1 and 10.")
    num = int(input("Enter a number between 1 and 10: "))

    print(f"ur number is {num}.")