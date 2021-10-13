def encrypt(message, key):
    key = key % 26
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    encrypted_message = ""
    for ch in message:
        if ch == " ":
            encrypted_message += ch
        else:
            index = letter_list.index(ch)
            index = (index + key) % 26
            encrypted_message += letter_list[index]

    return encrypted_message

def decrypt(encrypted_message, key):
    key = key % 26
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    decrypted_message = ""
    for ch in encrypted_message:
        if ch == " ":
            decrypted_message += ch
        else:
            index = letter_list.index(ch)
            index = (index - key) % 26
            decrypted_message += letter_list[index]

    return decrypted_message


message = input("Enter a message to encrypt: ")
key = int(input("Enter an encryption key: "))

encrypted_message = encrypt(message, key)
print(encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print(decrypted_message)