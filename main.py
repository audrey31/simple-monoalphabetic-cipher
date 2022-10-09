def inverse_monoalpha_cipher(monoalpha_cipher):
    inverse_monoalpha = {}
    for key, value in monoalpha_cipher.items():
        inverse_monoalpha[value] = key
    return inverse_monoalpha

def encrypt_with_monoalpha(message, monoalpha_cipher):
    encrypted_message = []
    for letter in message:
        encrypted_message.append(monoalpha_cipher.get(letter, letter))
    return ''.join(encrypted_message)

def decrypt_with_monoalpha(encrypted_message, monoalpha_cipher):
    return encrypt_with_monoalpha(
               encrypted_message,
               inverse_monoalpha_cipher(monoalpha_cipher)
           )
           
cipher = {'a': 'i', 'b': 'F', 'c': '3', 'd': '1', 'e': 'S', 'f': 'A', 'g': 'v', 'h': '5', 'i': 'e', 'j': '9', 'k': 'D', 'l': 'r', 'm': 'w', 'n': 'L', 'o': 's', 'p': 'R', 'q': '4', 'r': 'B', 's': 'H', 't': 'n', 'u': 'V', 'v': 'K', 'w': 'J', 'x': 'T', 'y': 'X', 'z': 'a', 'A': 'b', 'B': 'j', 'C': '7', 'D': 'Q', 'E': 'z', 'F': 'o', 'G': 'l', 'H': 'q', 'I': '8', 'J': 'P', 'K': 'M', 'L': 'h', 'M': 'I', 'N': 'W', 'O': 'N', 'P': 'k', 'Q': 'G', 'R': 'm', 'S': 't', 'T': '2', 'U': 'p', 'V': 'x', 'W': 'Z', 'X': 'g', 'Y': 'Y', 'Z': 'C', '0': 'u', '1': 'E', '2': 'd', '3': '0', '4': '6', '5': 'f', '6': 'c', '7': 'y', '8': 'O', '9': 'U'}
encrypted = encrypt_with_monoalpha('Jumps over the red roses', cipher)
print("Monoalphabetic encryption text:", encrypted)
decrypted = decrypt_with_monoalpha(encrypted, cipher)
print("Monoalphabetic decrypted text:", decrypted)
