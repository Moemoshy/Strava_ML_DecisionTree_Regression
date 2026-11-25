from cryptography.fernet import Fernet

def load_key():
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    return key

def decrypt_file(input_file_path, output_file_path):
    key = load_key()  # Load the key internally
    fernet = Fernet(key)
    with open(input_file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(output_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
