def extend_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def vigenere_encrypt(text, key):
    key = extend_key(text, key)
    cipher_text = []
    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ''.join(cipher_text)

def vigenere_decrypt(cipher_text, key):
    key = extend_key(cipher_text, key)
    original_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        original_text.append(chr(x))
    return ''.join(original_text)

# Використання
text = "HELLOPYTHON"
key = "CRYPTOGRAPHY"
encrypted_text = vigenere_encrypt(text, key)
print("Зашифрований текст:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Розшифрований текст:", decrypted_text)

