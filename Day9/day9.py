another_user = True
participants = {}

while another_user:
    participants[input("What's your name?\n")] = float(input("What's your bid?\n$"))
    if input("Are there any oher bidders? Type 'yes' or 'no': ") == 'yes':
        another_user = True
    else:
        another_user = False



higher_bid = 0
for key in participants:
    if participants[key] > higher_bid:
        higher_bid = participants[key]
        winner = key

print(f"The winner is {winner}, with a bid of ${higher_bid}")
