def caesar_decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr((((ord(char)+key)-97)% 26)+97)
            else:
                decrypted_char = chr((((ord(char)+key)-65)% 26)+65)
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

def brute_force_caesar(ciphertext):
    for key in range(-26, 27):
        decrypted_text = caesar_decrypt(ciphertext, key)
        print(f"Key {key}: {decrypted_text}")

if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext: ")
    brute_force_caesar(ciphertext)