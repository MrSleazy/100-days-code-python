# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)

MAX_AGE_YEARS = 90
MONTHS_IN_YEAR = 12
WEEKS_IN_YEAR = 52
DAYS_IN_YEAR = 365

remaining_years = (MAX_AGE_YEARS - age_int)

remaining_days = remaining_years * DAYS_IN_YEAR
remaining_weeks = remaining_years * WEEKS_IN_YEAR
remaining_months = remaining_years * MONTHS_IN_YEAR

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")
