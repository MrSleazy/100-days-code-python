# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0 
add_pepperoni_boolean = True if add_pepperoni == "Y" else False 
extra_cheese_boolean = True if extra_cheese == "Y" else False 
if size == "S":
    bill += 15
    if add_pepperoni_boolean:
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni_boolean:
        bill += 3
elif size == "L":
    bill += 25
    if add_pepperoni_boolean:
        bill += 3
else: 
    print("Invalid Size")
    
if extra_cheese_boolean: 
    bill += 1

print(f"Your final bill is: ${bill}.")