import math 
# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_rounded = round(weight / height ** 2)

if bmi_rounded <= 18.5:
    print(f"Your BMI is {bmi_rounded}, you are underweight.")
elif bmi_rounded <= 25:
    print(f"Your BMI is {bmi_rounded}, you have a normal weight.")
elif bmi_rounded <= 30:
    print(f"Your BMI is {bmi_rounded}, you are slightly overweight.")
elif bmi_rounded <= 35:
    print(f"Your BMI is {bmi_rounded}, you are obese.")
else: 
    print(f"Your BMI is {bmi_rounded}, you are clinically obese.")
