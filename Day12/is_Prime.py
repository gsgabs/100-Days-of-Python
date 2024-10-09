def is_prime(num):
    divisors = 0
    for number in range(1, num + 1):
        if num % number == 0:
            divisors += 1
    if divisors == 2:
        print(f"The number {num} is prime.")
    else:
        print(f"The number {num} isn't prime.")


user_desire = 'y'
while user_desire == 'y':
    is_prime(int(input("Type the number u wanna check is is Prime or not:  ")))
    user_desire = input("Again? type 'y' or 'n'.")
