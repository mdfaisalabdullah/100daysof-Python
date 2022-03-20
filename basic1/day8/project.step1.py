alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypt_word = ''
    for char in text:
        index = alphabet.index(char)
        encrypt_index = index + shift

        if encrypt_index <= 25:
            encrypt_word += alphabet[encrypt_index]
        
        ## what will happen if new index exceeded more than total alphabat
        if encrypt_index > 25:
            remain = 25 - index
            new_shift = shift - remain
            encrypt_word += alphabet[new_shift - 1]

    print(f"Your encrypted message is {encrypt_word}.")

def decrypt(text, shift):
    decrypt_word = ''
    for char in text:
        index = alphabet.index(char)
        decrypt_index = index - shift

        decrypt_word += alphabet[decrypt_index]

    print(f"Your decrypted message is {decrypt_word}.")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
