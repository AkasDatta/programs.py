
# 1. Tax

TAX_RATE_LOW = 0.02 
TAX_RATE_MEDIUM = 0.05 
TAX_RATE_HIGH = 0.1

LOW_THRESHOLD = 100
MEDIUM_THRESHOLD = 500
HIGH_THRESHOLD = 1000

print("Python Party Tax Program")

income = float(input("Income: $"))

total_tax = 0.0   

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

take_home_pay = income - total_tax

print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")


# 2. Car Insurance
age = int(input("Enter your age: "))
if age < 18:
    print("Hire refused")
elif age < 25:
    print("Insurance required")
else:
    print("Insurance not required")


# 3. Simple Password Checker

CORRECT_PASSWORD = "Jahid"

user_password = input("Enter your password: ")

if user_password == CORRECT_PASSWORD:
    print("Access granted")
else:
    print("Access denied")



# 4. Basketball

shots_attempted = int(input("Number of shots attempted: "))
shots_made = int(input("Number of shots made: "))

value = (shots_attempted  / shots_made) * 100

print(f"Your shooting percentage {value:.1f}%")

if value >= 80:
    print("That's great!")


# 5. Rock of Ages

age = int(input("Your current age: "))

if age < 0 or age > 120:
    print("Invalid age")
else:
    if age < 16:
        print("You are a child. Enjoy your childhood!")
    elif age < 21:
        print("You are a teenager. Embrace your youth!")
    elif age < 36:
        print("You are a young adult. Chase your dreams!")
    elif age < 60:
        print("You are an adult. Keep pushing forward!")
    else:
        print("You are a senior citizen. Enjoy your life and relax!")



# 6. Speeding Fines

speed = int(input("Your speed (km/h): "))
speed_limit = int(input("Speed limit (km/h): "))

speed_over_limit = speed - speed_limit

if speed_over_limit <= 0:
    print("You are within the speed limit. Please drive safely!")
else:
    if speed_over_limit <= 10:
        fine_amount = 309
    elif speed_over_limit <= 20:
        fine_amount = 464
    elif speed_over_limit <= 30:
        fine_amount = 696
    elif speed_over_limit <= 40:
        fine_amount = 1161
    else:
        fine_amount = 1780
    
    print(f"You were speeding! Your fine is: ${fine_amount}")


