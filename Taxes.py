income = float(input("Enter the annual income: "))
marital_status = input("Enter the marital status [y/n]: ")
if marital_status == "y":
  years_married = int(input("Enter the years married: "))

elevation = (input("Evevation below - 1 At sea level - 2 Above sea level - 3 "))

income_tax = 0
martial_adjustment = 0
additional_adjustment = 0

if income < 10000:
  income_tax = 0.023
elif 10000 <= income >= 50000:
  income_tax = 0.045
elif income > 50000:
  income_tax = 0.061

if marital_status == "y":
  years_married = int(input("Enter the years married: "))
  martial_adjustment = years_married * 1.62
elif marital_status == "n":
  martial_adjustment = 0

if elevation == "1":
  additional_adjustment = 18.32
elif elevation == "2":
  additional_adjustment = 0.016 * income
elif elevation == "3":
  bedrooms = int(input("How many bedrooms are in your house: "))
  additional_adjustment = 5 * bedrooms

total_tax = income * income_tax - martial_adjustment + additional_adjustment

print("Your tax total is: ", total_tax)









