def is_prime(num):
    divisors = 0
    for number in range(1, num + 1):
        if num % number == 0:
            divisors += 1
    if divisors == 2:
        return True
    else:
        return False


print(is_prime(73))