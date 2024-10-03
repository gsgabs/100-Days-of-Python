logo = ("""
                           _            _       _             
                  | |          | |     | |            
          ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
         / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
        | (_| (_| | | (__| |_| | | (_| | || (_) | |   
         \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
        
        """)
print(logo)


def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1/num2


first_number = float(input("What's the first number?:  "))
print("""
    +
    -
    *
    /
    """)
operation = input("Choose an operation:  ")
second_number = float(input("What's the next number?:  "))

print(f"{first_number} {operation} {second_number} = {calculate(first_number, second_number, operation)}")
