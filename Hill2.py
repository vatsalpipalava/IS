import numpy as np

# Substitution dictionary for mapping letters to numbers
substitution = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
               'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
               'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

# Inverse substitution dictionary for mapping numbers to letters
inverse_substitution = {value: key for key, value in substitution.items()}

def encrypt(plain_text, key_matrix):
    # Convert the plain text to uppercase
    plain_text = plain_text.upper()

    # Remove any spaces from the plain text
    plain_text = plain_text.replace(" ", "")

    # Pad the plain text if its length is not a multiple of the key matrix size
    if len(plain_text) % len(key_matrix) != 0:
        padding_length = len(key_matrix) - (len(plain_text) % len(key_matrix))
        plain_text += 'X' * padding_length

    # Initialize the cipher text
    cipher_text = ''

    # Encrypt the plain text
    for i in range(0, len(plain_text), len(key_matrix)):
        # Get the current block of the plain text
        block = plain_text[i:i+len(key_matrix)]

        # Convert the block to a column vector of numbers
        block_vector = np.array([substitution[ch] for ch in block])

        # Multiply the key matrix with the block vector
        encrypted_vector = np.dot(key_matrix, block_vector) % 26

        # Convert the encrypted vector back to a string
        encrypted_block = ''.join([inverse_substitution[num] for num in encrypted_vector])

        # Append the encrypted block to the cipher text
        cipher_text += encrypted_block

    return cipher_text

# Example usage
plain_text = 'HELLO WORLD'
key_matrix = np.array([[6, 24], [1, 13]])

cipher_text = encrypt(plain_text, key_matrix)
print("Cipher Text:", cipher_text)
