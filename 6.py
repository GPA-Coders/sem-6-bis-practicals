import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    m0, x0, x1 = phi, 0, 1
    while e > 1:
        q = e // phi
        m0, e, phi = phi, phi % e, e
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == "__main__":
    p = 61
    q = 53
    public, private = generate_keypair(p, q)
    message = "HELLO"
    encrypted_msg = encrypt(public, message)
    print("Encrypted message:", encrypted_msg)
    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted message:", decrypted_msg)

# Encrypted message: [2695, 1614, 2726, 2726, 1002]
# Decrypted message: HELLO