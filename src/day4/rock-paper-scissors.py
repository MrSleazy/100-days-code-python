import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

human_choice = int(input("What do you choose? 0 - rock, 1 - paper, 2 - scissors... "))

if human_choice > 2:
    raise ValueError("Must choose 0, 1 or 2")

choices = [rock, paper, scissors]

print(f"You chose: {choices[human_choice]}")

computer_choice = random.randint(0, 2)

print(f"Computer chose: {choices[computer_choice]}")

if human_choice == computer_choice:
    print("Tie game!")

elif human_choice == 0:
    if computer_choice == 1:
        print("You lose!")
    else:
        print("You win!")

elif human_choice == 1:
    if computer_choice == 2:
        print("You lose!")
    else:
        print("You win!")

elif human_choice == 2:
    if computer_choice == 0:
        print("You lose!")
    else:
        print("You win!")
