print("------------------------------------")
print("----- Ticket Pricing Software ------")
print("------------------------------------")

age = int(input("Enter your age"))

if (age <= 5):
    print("Free entry")
elif ((age > 5) and (age <= 18)):
    print("Entry fees is 900")
elif ((age > 18) and (age <= 40)):
    print("Entry fees is 1200")
else:
    print("Entry fees is 500")
