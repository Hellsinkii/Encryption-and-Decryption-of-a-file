from cryptography.fernet import Fernet
import os
def generate_key():
    key = Fernet.generate_key()
    with open("Secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("Secret.key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except InvalidToken:
            print("Invalid key")
            return
    with open(filename, "wb") as file:
        file.write(decrypted_data)

choice = input("Enter 'E' to encrypt or 'D' decrypt the file.").lower()
if choice == 'e':
    filename = input("Enter the file name to encrypt(including file extension):")
    if os.path.exists(filename):
        generate_key()
        key=load_key()
        encrypt(filename, key)
        print("File Encrypted Successfully!!!")
    else:
        print(f"file '{filename}' not found. Please check the file name and try again.")

elif choice == "d":
    filename = input("Enter the file name to encrypt(including file extension):")
    if os.path.exists(filename):
        key=load_key()
        decrypt(filename, key)
        print("File Decrypted Successfully!!!")
    else:
        print(f"file '{filename}' not found. Please check the file name and try again.")

else:
    print("Invalid choice. Please enter 'E' to encrypt a file or 'D' to decrypt a file")
