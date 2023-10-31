#Take plaintext from the user
plaintext=input("Enter the plaintext : ")

#Fix the key or we may take a dynamic key
key="xyzabcdefghijklmnopqrstuvw"

def encrypt(plaintext,key):
    cipher=""
    for i in plaintext:
        if i.isupper():
            cipher += key[ord(i)-65]
        elif i.islower():
            cipher += key[ord(i)-97]
        else:
            cipher += i
    return cipher
 
ciphertext= encrypt(plaintext,key)
print("Plaintext is " + plaintext + " Ciphertext is " + ciphertext)

def decrypt(ciphertext,key):
    plain=""
    for i in ciphertext:
        #print(key.find(i))
        if i.isupper():
            plain += chr(key.find(i)+65)
        elif i.islower():
            plain += chr(key.find(i)+97)
        else:
            plain += i
        
    return plain

plaintext= decrypt(ciphertext,key)
print("Ciphertext is " + ciphertext + " plaintext is " + plaintext)