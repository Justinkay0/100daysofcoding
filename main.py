from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
bidders = {}
while True:
    print(logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    if input("Are there an other bidders? Type 'yes' or 'no'.\n").lower() == 'no':
        break
    clear()
clear()
print(logo)
highest_bid = ""
amount = 1
for people in bidders:
    if bidders[people] > amount:
        highest_bid = people
        amount = bidders[people]

print(f"The winner is {highest_bid} with a bid of ${amount}")