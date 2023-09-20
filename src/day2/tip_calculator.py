import decimal
from math import ceil
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

bill_amount = float(input("What was the total amount? "))
tip_percentage = int(input("How much tip would you like to give? "))
if tip_percentage not in [10,12,15]:
    raise Exception("Not valid tip")
people_split = int(input("How many people to split the bill? "))

# bill_amount = float("2343.23")
# tip_percentage = int("15")
# people_split = int("7")

individual_amount = bill_amount / people_split
individual_tip = tip_percentage / 100 * individual_amount

# using format()
format_individual_amount = format(individual_amount, ".2f")
format_individual_tip = format(individual_tip, ".2f")
print(f"Thus everyone's share of the total bill is ${format_individual_amount} plus a ${format_individual_tip} tip.")

# using decimal lib
decimal_individual_amount = decimal.Decimal(individual_amount).quantize(decimal.Decimal('0.00'))
decimal_individual_tip = decimal.Decimal(individual_tip).quantize(decimal.Decimal('0.00'))
print(f"Thus everyone's share of the total bill is ${decimal_individual_amount} plus a ${decimal_individual_tip} tip.")

# using round()
round_individual_amount = round(individual_amount, 2)
round_individual_tip = round(individual_tip, 2)
print(f"Thus everyone's share of the total bill is ${round_individual_amount} plus a ${round_individual_tip} tip.")

# using ceil()
ceil_individual_amount = ceil(individual_amount * 100)/100
ceil_individual_tip = ceil(individual_tip * 100)/100
print(f"Thus everyone's share of the total bill is ${ceil_individual_amount} plus a ${ceil_individual_tip} tip.")





