import rsa
import hashlib

# Generate public and private keys (2048 bits)
public_key, private_key = rsa.newkeys(2048)

def sign(message, private_key):
    # Compute the SHA-256 hash of the message
    message_hash = hashlib.sha256(message.encode()).digest()
    
    # Sign the hash with the private key
    signature = rsa.sign(message_hash, private_key, 'SHA-256')
    
    return signature

def verify(message, signature, public_key):
    # Compute the SHA-256 hash of the message
    message_hash = hashlib.sha256(message.encode()).digest()
    
    try:
        # Verify the signature with the public key
        rsa.verify(message_hash, signature, public_key)
        return True
    except rsa.VerificationError:
        return False

# Test the digital signature algorithm
message = "Hello, World!"
signature = sign(message, private_key)

if verify(message, signature, public_key):
    print("The signature is valid.")
else:
    print("The signature is invalid.")