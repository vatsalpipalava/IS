import hashlib

# Function to generate SHA-1 hash
def generate_sha1_hash(input_string):
    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()
    return sha1_hash

# Example usage
if __name__ == "__main__":
    input_string = input("Enter the string to generate SHA-1 hash: ")
    sha1_hash = generate_sha1_hash(input_string)
    print("SHA-1 hash:", sha1_hash)