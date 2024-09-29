print("Welcome to tip calculator!")
bill = float(input("What was the total bill? R$"))
tip = float(input("How much percentage tip would u like to give? "))/100
people = int(input("How many people are going to share it? "))
tte = (bill * tip)/people
tte = round(tte, 2)
print(f"Each one should pay R${tte}")
