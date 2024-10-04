def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True
    if leap:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} isn't a leap year.")


print("Welcome to leap year checker")
year_input = int(input("Which year you wanna check if is leap?:  "))
is_leap_year(year_input)
