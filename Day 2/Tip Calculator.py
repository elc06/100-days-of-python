print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))
tip_amount = bill*(tip/100)
total_bill = (bill+tip_amount)/people
print(f"Each person should pay: ${total_bill}")