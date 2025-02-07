from art import *

tprint("Bidding")

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bidder_amount = bidding_dictionary[bidder]
        if bidder_amount > highest_bid:
            highest_bid = bidder_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bid = {}
continue_bidding = True

while continue_bidding:
    name = input("Please enter your name:\n")
    bid_amount = int(input("Please enter the bid amount:\n"))
    bid[name] = bid_amount
    next_bid_amount = input("Are there are any other bidders: if Yes, Please Enter or else No:\n").lower()
    if next_bid_amount == "no":
        continue_bidding = False
        find_highest_bidder(bid)