
# Q1 - Electricity Subsidy Eligibility

units = int(input("Enter electricity units: "))
ration = input("Do you have a ration card (yes/no): ").lower()
senior = input("Is any member above 80 years (yes/no): ").lower()

print("\nUsing separate if statements:")

if units <= 100:
    print("Full subsidy")

if 101 <= units <= 200 and ration == "yes":
    print("Partial subsidy")

if units > 200 and senior == "yes":
    print("Special subsidy")

if units > 200 and senior != "yes":
    print("No subsidy")

print("\nUsing if-elif-else:")

if units <= 100:
    print("Full subsidy")
elif 101 <= units <= 200 and ration == "yes":
    print("Partial subsidy")
elif 101 <= units <= 200:
    print("No subsidy")
elif units > 200 and senior == "yes":
    print("Special subsidy")
else:
    print("No subsidy")
