# Constants for tax rates and thresholds
TAX_RATE_LOW = 0.02  # 2% for income between $100 and $500
TAX_RATE_MEDIUM = 0.05  # 5% for income between $500 and $1000
TAX_RATE_HIGH = 0.1  # 10% for income above $1000

LOW_THRESHOLD = 100
MEDIUM_THRESHOLD = 500
HIGH_THRESHOLD = 1000

# Program Title
print("Python Party Tax Program - Tax Simplified")

# Take input from the  user
income = float(input("Enter your income: $"))

# Initialize total tax to 0
total_tax = 0.0   # That's Default (for incomes below $100)

# Calculate tax based on income
if income <= LOW_THRESHOLD:
    total_tax = 0
elif income <= MEDIUM_THRESHOLD:
    total_tax = (income - LOW_THRESHOLD) * TAX_RATE_LOW
elif income <= HIGH_THRESHOLD:
    total_tax = (MEDIUM_THRESHOLD - LOW_THRESHOLD) * TAX_RATE_LOW + (income - MEDIUM_THRESHOLD) * TAX_RATE_MEDIUM
else:
    total_tax = (MEDIUM_THRESHOLD - LOW_THRESHOLD) * TAX_RATE_LOW + \
                (HIGH_THRESHOLD - MEDIUM_THRESHOLD) * TAX_RATE_MEDIUM + \
                (income - HIGH_THRESHOLD) * TAX_RATE_HIGH

# Calculate take-home pay
take_home_pay = income - total_tax

#  Output the total and take-home pay
print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")


################## 2. Car Insurance
age = int(input("Enter your age: "))
if age < 18:
    print("Hire refused")
elif age < 25:
    print("Insurance required")
else:
    print("Insurance not required")


################
### 3. Simple Password Checker

CORRECT_PASSWORD = "Jahid"

user_password = input("Enter your password: ")

if user_password == CORRECT_PASSWORD:
    print("Access granted")
else:
    print("Access denied")