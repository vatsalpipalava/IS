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
    # Find the row and column of a character in the matrix
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return (row, col)

def playfair_encrypt(plain_text, key):
    # Build the Playfair matrix using the provided key
    matrix = build_playfair_matrix(key)
    # Prepare the plain text by removing spaces, converting to uppercase, and replacing 'J' with 'I'
    plain_text = prepare_text(plain_text)
    # Initialize an empty list to store the encrypted text
    encrypted_text = []
    i = 0
    # Iterate through the plain text in pairs
    while i < len(plain_text):
        char1 = plain_text[i]
        char2 = plain_text[i + 1]
        # Find the positions (row and column) of the characters in the matrix
        row1, col1 = find_char_positions(matrix, char1)
        row2, col2 = find_char_positions(matrix, char2)
        if row1 == row2:  # Same row
            # Characters are in the same row, so shift to the right (circularly) in the same row
            encrypted_text.append(matrix[row1][(col1 + 1) % 5])
            encrypted_text.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:  # Same column
            # Characters are in the same column, so shift downwards (circularly) in the same column
            encrypted_text.append(matrix[(row1 + 1) % 5][col1])
            encrypted_text.append(matrix[(row2 + 1) % 5][col2])
        else:
            # Characters are in different rows and columns, form a rectangle, replace with opposite corners
            encrypted_text.append(matrix[row1][col2])
            encrypted_text.append(matrix[row2][col1])
        i += 2
    # Join the encrypted characters and return the encrypted text
    return ''.join(encrypted_text)

def playfair_decrypt(cipher_text, key):
    # Build the Playfair matrix using the provided key
    matrix = build_playfair_matrix(key)
    # Initialize an empty list to store the decrypted text
    decrypted_text = []
    i = 0
    # Iterate through the cipher text in pairs
    while i < len(cipher_text):
        char1 = cipher_text[i]
        char2 = cipher_text[i + 1]
        # Find the positions (row and column) of the characters in the matrix
        row1, col1 = find_char_positions(matrix, char1)
        row2, col2 = find_char_positions(matrix, char2)
        if row1 == row2:  # Same row
            # Characters are in the same row, so shift to the left (circularly) in the same row
            decrypted_text.append(matrix[row1][(col1 - 1) % 5])
            decrypted_text.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Same column
            # Characters are in the same column, so shift upwards (circularly) in the same column
            decrypted_text.append(matrix[(row1 - 1) % 5][col1])
            decrypted_text.append(matrix[(row2 - 1) % 5][col2])
        else:
            # Characters are in different rows and columns, form a rectangle, replace with opposite corners
            decrypted_text.append(matrix[row1][col2])
            decrypted_text.append(matrix[row2][col1])
        i += 2
    # Join the decrypted characters and return the decrypted text
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

