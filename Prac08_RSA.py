# Get user input for p, q, M, and e
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))
M = int(input("Enter the message (M): "))
e = int(input("Enter public exponent (e): "))

# Calculate n, phi(n), d, public key, and private key based on user input
n = p * q
phi = (p - 1) * (q - 1)

# d = e^-1 mod phi
d = pow(e, -1, phi)
print("d =",d)

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