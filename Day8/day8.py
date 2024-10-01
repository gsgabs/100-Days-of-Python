alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z"
]

direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(message, shift_number):
    encrypted_message = ''
    for letter in message:
        if letter == ' ':
            encrypted_message += ' '
        else:
            encrypted_message += alphabet[alphabet.index(letter) + shift_number]
    return encrypted_message


def decrypt(message, shift_number):
    decrypted_message = ''
    for letter in message:
        if letter == ' ':
            decrypted_message += ' '
        else:
            decrypted_message += alphabet[alphabet.index(letter) - shift_number]
    return decrypted_message


encrypt(text, shift)
