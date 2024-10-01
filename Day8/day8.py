alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z"
]

logo = [
    """

     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba, 
    a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8
    8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
                  88                                             
                  88
    """
    ]
print(logo)
direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(message, shift_number):
    encrypted_message = ''
    for letter in message:
        if letter == ' ':
            encrypted_message += ' '
        elif letter not in alphabet:
            encrypted_message += letter
        else:
            position = alphabet.index(letter) + shift_number
            if position >= 26:
                position -= 26
            encrypted_message += alphabet[position]
    print(f"Here's the encoded result: {encrypted_message}")


def decrypt(message, shift_number):
    decrypted_message = ''
    for letter in message:
        if letter == ' ':
            decrypted_message += ' '
        elif letter not in alphabet:
            decrypted_message += letter
        else:
            position = alphabet.index(letter) - shift_number
            if position < 0:
                position += 26
            decrypted_message += alphabet[position]
    print(f"Here's the decoded result: {decrypted_message}")


if direction == "decode":
    decrypt(text, shift)
else:
    encrypt(text, shift)
