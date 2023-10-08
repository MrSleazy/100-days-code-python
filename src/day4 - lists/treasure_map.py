line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
# position = input()  # Where do you want to put the treasure?
position = "B3"  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

characters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
letter_index = characters.index(position[0].lower())
number_index = int(position[1]) - 1
# print(f"{letter_index} {number_index}")

map[letter_index][number_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
