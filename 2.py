def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += char
    return result


if __name__ == "__main__":
    plaintext = "hello"
    key = 3
    plaintext = plaintext.upper()
    
    ciphertext = caesar_encrypt(plaintext, key)
    print(f"Cipher text: {ciphertext}")

    plaintext = caesar_decrypt(ciphertext, key)
    print(f"Plain Text: {plaintext}")

# Cipher text: KHOOR
# Plain Text: HELLO