def getKeyMatrix(key):
    keyMatrix = [[0] * 3 for i in range(3)]
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    return keyMatrix

def encrypt(messageVector, keyMatrix):
    cipherMatrix = [[0] for i in range(3)]
    for i in range(3):
        for j in range(1):
            for x in range(3):
                cipherMatrix[i][j] += keyMatrix[i][x] * messageVector[x][j]
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
    return cipherMatrix

def HillCipher(message, key):
    keyMatrix = getKeyMatrix(key)
    messageVector = [[0] for i in range(3)]
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
    cipherMatrix = encrypt(messageVector, keyMatrix)
    CipherText = [chr(cipherMatrix[i][0] + 65) for i in range(3)]
    
    return "".join(CipherText)

if __name__ == "__main__":
    message = "ACT"
    key = "GYBNQKURP"
    ciphertext = HillCipher(message, key)
    print(f"Cipher Text: {ciphertext}")

# Cipher Text: POH