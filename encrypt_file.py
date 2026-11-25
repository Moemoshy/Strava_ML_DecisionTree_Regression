from cryptography.fernet import Fernet

def load_key():
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_file(input_file_path, output_file_path):
    key = load_key()  # Load the key internally
    fernet = Fernet(key)
    with open(input_file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(output_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
