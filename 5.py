def encryptRailFence(text, key):
    rail = [''] * key
    layer = 0
    step = 1
    for char in text:
        rail[layer] += char
        layer += step
        if layer == 0 or layer == key - 1:
            step = -step
    return ''.join(rail)

if __name__ == "__main__":
    text = "INFORMATIONSECURITY"
    key = 3
    encrypted = encryptRailFence(text, key)
    print(f"Cipher Text: {encrypted}")

# Cipher Text: IRIEINOMTOSCRTFANUY