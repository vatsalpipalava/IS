# Initialize the key matrix, message vector, and cipher matrix
keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]

# Function to populate the key matrix from the input key
def getKeyMatrix(key):
    k = 0
    # Iterate over the rows and columns of the key matrix
    for i in range(3):
        for j in range(3):
            # Convert characters to integers and store in the key matrix
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

# Function to perform encryption using Hill Cipher algorithm
def encrypt(messageVector):
    # Iterate through rows of key matrix
    for i in range(3):
        # Iterate through columns of message vector (which is a column matrix)
        for j in range(1):
            cipherMatrix[i][j] = 0
            # Perform matrix multiplication and modular arithmetic
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

# Hill Cipher implementation
def HillCipher(message, key):
    # Populate the key matrix
    getKeyMatrix(key)
    # Convert characters of the message to integers and store in message vector
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
    # Encrypt the message vector
    encrypt(messageVector)
    CipherText = []
    # Convert encrypted integers back to characters and append to CipherText list
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
    # Print the encrypted message
    print("Ciphertext: ", "".join(CipherText))

# Main function to take user input and call HillCipher function
def main():
    message = input("Enter the message to be encrypted: ").upper()
    key = input("Enter the key: ").upper()
    HillCipher(message, key)

# Entry point of the program
if __name__ == "__main__":
    main()