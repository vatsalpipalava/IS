import re

def prepare_text(text):
    # Remove spaces and convert to uppercase
    text = re.sub(r'[^A-Za-z]', '', text.upper())
    # Replace 'J' with 'I' (Playfair does not use 'J')
    text = text.replace("J", "I")
    return text

def build_playfair_matrix(key):
    key = prepare_text(key)
    # Initialize a 5x5 matrix with zeros
    matrix = [['' for _ in range(5)] for _ in range(5)]
    used_chars = set()
    chars = key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    for char in chars:
        if char not in used_chars:
            row, col = divmod(len(used_chars), 5)
            matrix[row][col] = char
            used_chars.add(char)
    
    return matrix

def find_char_positions(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return (row, col)

def playfair_encrypt(plain_text, key):
    matrix = build_playfair_matrix(key)
    plain_text = prepare_text(plain_text)
    encrypted_text = []
    i = 0
    while i < len(plain_text):
        char1 = plain_text[i]
        char2 = plain_text[i + 1]
        row1, col1 = find_char_positions(matrix, char1)
        row2, col2 = find_char_positions(matrix, char2)
        if row1 == row2:  # Same row
            encrypted_text.append(matrix[row1][(col1 + 1) % 5])
            encrypted_text.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:  # Same column
            encrypted_text.append(matrix[(row1 + 1) % 5][col1])
            encrypted_text.append(matrix[(row2 + 1) % 5][col2])
        else:
            encrypted_text.append(matrix[row1][col2])
            encrypted_text.append(matrix[row2][col1])
        i += 2
    return ''.join(encrypted_text)

def playfair_decrypt(cipher_text, key):
    matrix = build_playfair_matrix(key)
    decrypted_text = []
    i = 0
    while i < len(cipher_text):
        char1 = cipher_text[i]
        char2 = cipher_text[i + 1]
        row1, col1 = find_char_positions(matrix, char1)
        row2, col2 = find_char_positions(matrix, char2)
        if row1 == row2:  # Same row
            decrypted_text.append(matrix[row1][(col1 - 1) % 5])
            decrypted_text.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Same column
            decrypted_text.append(matrix[(row1 - 1) % 5][col1])
            decrypted_text.append(matrix[(row2 - 1) % 5][col2])
        else:
            decrypted_text.append(matrix[row1][col2])
            decrypted_text.append(matrix[row2][col1])
        i += 2
    return ''.join(decrypted_text)

# Take user input for key and plaintext
key = input("Enter the key: ")
plaintext = input("Enter the plaintext: ")

# Encrypt the plaintext
encrypted_text = playfair_encrypt(plaintext, key)
print("Encrypted: ", encrypted_text)

# Decrypt the ciphertext
decrypted_text = playfair_decrypt(encrypted_text, key)
print("Decrypted: ", decrypted_text)
