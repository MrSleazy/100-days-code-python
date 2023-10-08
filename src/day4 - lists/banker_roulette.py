from os import name
import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

print(f"{names[random.randrange(0, len(names))]} is going to buy the meal today!")
