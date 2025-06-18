logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print("Hello, welcome to The Secret Auction Program!")
print(logo)

bid_mode = True
price = {}          #Dictionary to store usernames and their bids

while bid_mode:
    user_name = input("What is your name?\n")
    user_bid = input("What is your bid?\n")

    price[user_name] = user_bid #Store user & bid to the dictionary

    other_bidder = input("Are there any other bidders: Y or N\n").upper()

    print("\n" * 20)            #Clear the screen for the next user

    if other_bidder == "N":     #Exit the while loop -- End the auction program
        bid_mode = False

#Find the auction winner
highest_bid = 0
winner = ""

for user in price:          #Loop through each key in the dictionary
    bid = int(price[user])  #Convert bid value from string to integer

    if bid > highest_bid:
        highest_bid = bid
        winner = user
print(f"The winner is {winner} with a bit of ${highest_bid}.")