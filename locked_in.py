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

#num = int(input("Enter a number between 1 and 10: "))
# while "num < 1" is true or "num > 10"is true: execute this code 4 ever
#while num < 1 or num > 10:
#   print(f"{num} is not between 1 and 10.")
#    num = int(input("Enter a number between 1 and 10: "))

#    print(f"ur number is {num}.")

#.......................................................................................................................
# python compound interest calculator

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount (greater than 0): "))
    if principal <= 0:
        print("Principal amount must be greater than 0. Please try again.")


while rate <= 0:
    rate = float(input("Enter the annual interest rate (as a percentage, greater than 0): "))
    if rate <= 0:
        print("Interest rate must be greater than 0. Please try again.")


while time <= 0:
    time = int(input("Enter the time period (in years, greater than 0): "))
    if time <= 0:
        print("Time period must be greater than 0. Please try again.")


print(f"Principal amount entered: {principal}")

print(f"Interest rate entered: {rate}")

print(f"Time period entered: {time}")

total = principal * pow(1 + rate / 100, time)
print(f"Balance after {time} years: ${total:.2f}")
