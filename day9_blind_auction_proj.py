# from replit import clear
from os import system
# system('cls')
#HINT: You can call clear() to clear the output in the console.

from blind_auction_art import logo

print(logo)

name_bid_dict = {}

wanting_continue = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"[+] 축하드립니다! 낙찰자는 {winner}님이며, 낙찰가격은 ${highest_bid}입니다! [+]")

while wanting_continue:
    name = input("이름이 어떻게 되시나요? : ")

    bid = input("얼마를 입찰하시겠습니까? :\n$")

    name_bid_dict[name] = bid

    another_bidder = input("다른 입찰자가 존재합니까? (y/n) : ").lower()

    if another_bidder == "y":
        system('cls')
    elif another_bidder == "n":
        wanting_continue = False 
        
find_highest_bidder(bidding_record=name_bid_dict)   

