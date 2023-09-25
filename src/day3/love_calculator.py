# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
# name1 = "Angela Yu"
# name2 = "Jack Bauer"


names_lowered = name1.lower() + name2.lower()

first_digit_count = 0
second_digit_count = 0

first_digit_count += names_lowered.count("t")
first_digit_count += names_lowered.count("r")
first_digit_count += names_lowered.count("u")
first_digit_count += names_lowered.count("e")

second_digit_count += names_lowered.count("l")
second_digit_count += names_lowered.count("o")
second_digit_count += names_lowered.count("v")
second_digit_count += names_lowered.count("e")

love_result = int(f"{first_digit_count}{second_digit_count}")

if love_result < 10 and love_result > 90:
    print(f"Your score is {love_result}, you go together like coke and mentos.")
elif love_result >= 40 and love_result <= 50:
    print(f"Your score is {love_result}, you are alright together.")
else:
    print(f"Your score is {love_result}")
