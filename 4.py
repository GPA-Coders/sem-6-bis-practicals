def toLowerCase(text):
    return text.lower()

def removeSpaces(text):
    newText = ""
    for i in text:
        if i != " ":
            newText += i
    return newText

def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text) + 1, 2):
        Diagraph.append(text[group:i])
        group = i
    if len(text) % 2 != 0:
        Diagraph[-1] += 'z'
    return Diagraph

def FillerLetter(text):
    k = len(text)
    new_word = text
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + 'x' + text[i+1:]
                new_word = FillerLetter(new_word)
                break
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + 'x' + text[i+1:]
                new_word = FillerLetter(new_word)
                break
    return new_word

def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)
    compElements = key_letters[:]
    for i in list1:
        if i not in compElements:
            compElements.append(i)
    matrix = []
    while compElements:
        matrix.append(compElements[:5])
        compElements = compElements[5:]
    return matrix

def search(mat, element):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == element:
                return i, j

def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    return matr[e1r][(e1c + 1) % 5], matr[e2r][(e2c + 1) % 5]

def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    return matr[(e1r + 1) % 5][e1c], matr[(e2r + 1) % 5][e2c]

def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    return matr[e1r][e2c], matr[e2r][e1c]

def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in plainList:
        ele1_x, ele1_y = search(Matrix, i[0])
        ele2_x, ele2_y = search(Matrix, i[1])
        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        CipherText.append(c1 + c2)
    return "".join(CipherText)

if __name__ == "__main__":
    text_Plain = 'instruments'
    key = "Monarchy"
    text_Plain = removeSpaces(toLowerCase(text_Plain))
    PlainTextList = Diagraph(FillerLetter(text_Plain))
    key = toLowerCase(key)
    Matrix = generateKeyTable(key, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    # Matrix = generateKeyTable(key, ['a', 'b', 'c', 'd' .. 'z'])
    CipherText = encryptByPlayfairCipher(Matrix, PlainTextList)
    print(f"Cipher Text: {CipherText}")

# Cipher Text: gatlmzclrq