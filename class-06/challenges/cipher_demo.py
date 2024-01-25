def encrypt(number, key):
    encrypted_text = ""

    for num in number:
        numb = int(num, 16)
        shifted_num = (numb + key) % 10
        encrypted_text += str(shifted_num)

    return encrypted_text


def decrypt(encoded, key):
    return encrypt(encoded, -key)

if __name__ == "__main__":
    encrypted = encrypt('1234567', 3)
    print(encrypted)
    decrypted = decrypt(encrypted, 3)
    print(decrypted)
