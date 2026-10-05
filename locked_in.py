# guessing game man
import random

rolling = True 
while rolling:
    choice= input("Roll the dice? (k/n): ").lower()
    if choice == "k":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"{die1, die2}")
    elif choice == "n":
        print("thank u fam for playing")
        break 
else:
    print("invalid choice!")
