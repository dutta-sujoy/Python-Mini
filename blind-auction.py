from replit import clear
logo = '''
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

print(logo)
bid ={}
bid_finish = False

def find_winer(bid_record):
  highest_bid = 0
  winner ="none"
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
    
  print(f"The Winner is {winner} with the bid of ${highest_bid} ") 



while not bid_finish:
  name = input("Your name:")
  price = int(input("Your bid $:"))
  bid[name] = price
  other = input("Is there is any other bider ? type 'yes' or 'no': \n")
  if other == "no":
    bid_finish = True
    find_winer(bid)
  elif other == "yes":
    clear()

