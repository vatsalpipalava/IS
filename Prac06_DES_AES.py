#DES
from Crypto.Cipher import DES

def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

key = b'abcdefgh'
des = DES.new(key, DES.MODE_ECB)

text = b'Python is the Best Language!'
padded_text = pad(text)

print("----------DES----------")

encrypted_text = des.encrypt(padded_text)
print("DES Encrypted Data: ", encrypted_text)

decrypted_text = des.decrypt(encrypted_text)
print("DES Decrypted Data: ", decrypted_text)

#AES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(mode, key, data):
    cipher = AES.new(key, mode)
    if isinstance(data, str):
        data = data.encode()
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return ct_bytes

def aes_decrypt(mode, key, encrypted_data):
    cipher = AES.new(key, mode)
    decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted

key = get_random_bytes(16)
data = "Python is the Best Language!"
mode = AES.MODE_ECB

print("----------AES----------")

# Encrypt the data
encrypted_data = aes_encrypt(mode, key, data)
print("AES Encrypted Data: ", encrypted_data)

# Decrypt the data
decrypted_data = aes_decrypt(mode, key, encrypted_data)
print("AES Decrypted Data: ", decrypted_data.decode())