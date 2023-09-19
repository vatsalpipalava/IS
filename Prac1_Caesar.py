# Caesar Cipher Encryption Decryption and Crypt Analysis
plaintext = input("Enter the Text : ")
key = int(input("Enter the value of key : "))

# Encryption of Plain text to Cipher text
def encrypt(p,k):
    cipher=""
    for i in p:
        if i.isupper():
            cipher += chr((((ord(i)+k)-65)% 26)+65) 
        else:
            cipher += chr((((ord(i)+k)-97)% 26)+97)
    return cipher
    
ciphertext = encrypt(plaintext,key)
print("Ciphertext for the plain text :",plaintext," is ",ciphertext)


# Decrption of Cipher text to Plain text
def decrypt(c,k):
    plain=""
    for i in c:
        if i.isupper():
            plain += chr((((ord(i)-k)-65)% 26)+65)
        else:
            plain += chr((((ord(i)-k)-97)% 26)+97)
    return plain

decrypted_plain = decrypt(ciphertext,key)
print("Plaintext for the cipher text :",ciphertext," is ",decrypted_plain)


# Crypt Analysis(Brute Force Attack) of caeser cipher to get key from the cipher text 
def crypt_analysis(c,p):
    for j in range(1,26):
        plain=""
        for i in c:
            if i.isupper():
                plain += chr((((ord(i)-j)-65)% 26)+65)
            else:
                plain += chr((((ord(i)-j)-97)% 26)+97)
        if(plain == p):
            break
    return j
    
k = crypt_analysis(ciphertext,plaintext)
print("Key after crypt_analysis : ",k)