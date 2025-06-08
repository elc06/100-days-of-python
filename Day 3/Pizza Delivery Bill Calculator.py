print("Welcome to McPizza's Delivery")

size = input("What size pizza do you want? S, M, L:\n").upper()
add_on_pepperoni = input("Would you like to add pepperoni on your pizza? Y or N:\n").upper()
add_on_cheese = input("Do you want extra cheese? Y or N:\n").upper()

bill = 0

if size == "S":
   bill += 15
elif size == "M":
   bill += 20
elif size == "L":
   bill += 25
else:
   print("You have chosen an invalid size. Please try again.")
   exit()

if add_on_pepperoni == "Y":
   bill += 2 if size == "S" else 3

if add_on_cheese == "Y":
   bill += 1

print(f"Your total is ${bill}.\nYour order will be ready within 20 - 30 minutes.")