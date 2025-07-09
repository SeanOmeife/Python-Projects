# Python compound interest calculator

# Initialise variables for principle, rate, and time
principle = 0
rate = 0
time = 0

# Input and validate the principle amount
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

# Input and validate the interest rate
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break

# Input and validate the time in years
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than or equal to zero")
    else:
        break
        
# Calculate compound interest using the formula: A = P * (1 + r/100)^t
total = principle * pow((1 + rate / 100), time)

# Display the final balance after the specified time
print(f"Balance after {time} year/s: €{total:.2f}")

