# Encryption
plaintext = input("Enter message: ")
plaintext = plaintext.upper()

key = input("Enter key: ")
key = key.upper()
dim = 3
m = []

for i in range(0, len(key), dim):
    m.append([ord(key[i]) - 65,
              ord(key[i+1]) - 65,
              ord(key[i+2]) - 65])

ciphertext = ""
for i in range(0, len(plaintext), dim):
    lm = []

    for a in range(3):
        try:
            lm.append(ord(plaintext[i+a]) - 65)
        except Exception:
            lm.append(0)
    
    mm = []
    for j in range(dim):
        s = 0
        for k in range(dim):
            s += m[j][k] * lm[k]
        mm.append((s % 26) + 65)
    
    for i in mm:
        ciphertext += chr(i)

print(f"Cipher Text: {ciphertext}")