################## 1. Tax Program

tax_low = 0.02  ### 2% for income $(100-500)
tax_medium = 0.05  # 5% for income $(500-1000)
tax_high = 0.1  # 10% for income above $1000

low_limit = 100
mid_limit = 500
high_limit = 1000

print("Python Party Tax Program - Tax Simplified")
income = float(input("Enter your income: $"))

# Calculate tax
if income < low_limit:
    tax = 0
elif income <= mid_limit:
    tax = (income - low_limit) * tax_low
elif income <= high_limit:
    tax = (mid_limit - low_limit) * tax_low + (income - mid_limit) * tax_medium
else:
    tax = (mid_limit - low_limit) * tax_low + (high_limit - mid_limit) * tax_medium + (income - high_limit) * tax_high

# Calculate take-home pay
take_home_pay = income - tax

# Display results
print("Total tax: $", tax, sep="")
print("Take home pay: $", take_home_pay, sep="")
