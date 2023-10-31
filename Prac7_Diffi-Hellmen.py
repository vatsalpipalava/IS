# Function to calculate (base^exp) % mod using modular exponentiation
def mod_exp(base, exp, mod):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        temp = mod_exp(base, exp // 2, mod)
        return (temp * temp) % mod
    else:
        temp = mod_exp(base, exp // 2, mod)
        return (base * temp * temp) % mod

# Diffie-Hellman Key Exchange Function
def diffie_hellman(prime, generator, private_key):
    public_key = mod_exp(generator, private_key, prime)
    return public_key

# Example usage
if __name__ == "__main__":
    # Commonly agreed prime and generator values
    prime = 101  # Prime number (p)
    generator = 37  # Generator (g)

    # Alice's private key
    alice_private_key = 60

    # Bob's private key
    bob_private_key = 73

    # Calculate public keys for Alice and Bob
    alice_public_key = diffie_hellman(prime, generator, alice_private_key)
    bob_public_key = diffie_hellman(prime, generator, bob_private_key)

    # Shared secret calculation
    alice_shared_secret = mod_exp(bob_public_key, alice_private_key, prime)
    bob_shared_secret = mod_exp(alice_public_key, bob_private_key, prime)

    # Both Alice and Bob should have the same shared secret
    print("Alice's Shared Secret:", alice_shared_secret)
    print("Bob's Shared Secret:", bob_shared_secret)