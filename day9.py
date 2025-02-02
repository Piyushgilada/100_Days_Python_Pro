print("Welcome to the secret auction program.")
bids = {}  # Initialize an empty dictionary to store all bids
flag = "yes"
while flag == "yes":
    # Collect user input
    user_name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    # Save bid in the dictionary
    bids[user_name] = price
    # Ask if there are more bidders
    flag = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
def highest_bider(bidding_dicts):
    highest_bid=0
    winner=''
    for bidder in bidding_dicts:
        bid_amount=bidding_dicts[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"winner is {winner} with a bid {highest_bid}")

highest_bider(bids)