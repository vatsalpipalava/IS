def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Get user input for p, q, M, and e
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))
M = int(input("Enter the message (M): "))
e = int(input("Enter public exponent (e): "))

# Calculate n, phi(n), d, public key, and private key based on user input
n = p * q
phi = (p - 1) * (q - 1)
d = mod_inverse(e, phi)

public_key = (e, n)
private_key = (d, n)

# Print public and private keys
print("\nPublic Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

# Encryption
C = pow(M, e, n)
print("\nEncryption:")
print("C =", M, "^", e, "mod", n, "=", C)

# Decryption
decrypted_msg = pow(C, d, n)
print("\nDecryption:")
print("M =", C, "^", d, "mod", n, "=", decrypted_msg)