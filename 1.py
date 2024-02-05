# Encryption
plaintext = input("Enter message: ")
plaintext = plaintext.upper()

key = 3

ciphertext = ""
for l in plaintext:
    ciphertext += chr(((ord(l) - 65 + key) % 26) + 65)

print(f"Cipher Text: {ciphertext}")

# Enter message: hello
# Cipher Text: KHOOR

# Decryption
ciphertext = input("Enter Cipher Text: ")
ciphertext = ciphertext.upper()

key = 3

plaintext = ""
for l in ciphertext:
    plaintext += chr(((ord(l) - 65 - key) % 26) + 65)

print(f"Plain Text: {plaintext}")

# Enter Cipher Text: khoor
# Plain Text: HELLO