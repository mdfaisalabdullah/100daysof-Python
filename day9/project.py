## auction bidding
import os  # os module importing for clear console

auction = {}
bidding_remain = True

while bidding_remain:
    name = input("What is your name? : ")
    bid = input("What is your bid? : ")

    ## set name(key) and bid(value) into auction dictionary
    auction[name] = bid

    remain = input("Is there anyone remaining to bid?yes or no? : ")

    ## should auction goes on?
    if remain == "no":
        bidding_remain = False

    ## clearing console after one bid
    os.system("cls")


auction_names = []
auction_bids = []


## for every name and bid in the auction dictionary, take all names and bids into different list

for name in auction:
    auction_names.append(name)
    auction_bids.append(auction[name])


## find maximum bid
maximum_bid = max(auction_bids)


## finding maximum bid index because of finding corresponding bid's name
i = auction_bids.index(maximum_bid)

print(f"{auction_names[i]} won, because of bidding of {maximum_bid}.")
