from cryptography.fernet import Fernet
import getpass
import re
import os

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

def save_credentials(username, encrypted_password):
    with open('user_data.txt', 'w') as f:
        f.write(username + '\n')
        f.write(encrypted_password.decode() + '\n')

def load_credentials():
    with open('user_data.txt', 'r') as f:
        lines = f.readlines()
        username = lines[0].strip()
        encrypted_password = lines[1].strip().encode()
        return username, encrypted_password

def valid_username(username):
    regex = "^(?!.\.\.)(?!.\.$)[^\W][\w.]{0,29}$"
    p = re.compile(regex)
    if (username == None):
        return False
    if(re.search(p, username)):
        return True
    else:
        return False

if not os.path.exists('key.key'):
    generate_key()

key = load_key()

while True:
    print("1. Encrypt and save password")
    print("2. Decrypt password")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter your username: ")
        while not valid_username(username):
            print("Invalid username. Try again.")
            username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        encrypted_password = encrypt_password(password, key)
        save_credentials(username, encrypted_password)
        print("Encrypted username and password have been saved to 'user_data.txt'")

    elif choice == '2':
        entered_username = input("Enter your username: ")
        username, encrypted_password = load_credentials()
        if entered_username == username:
            decrypted_password = decrypt_password(encrypted_password, key)
            print(f"Decrypted password: {decrypted_password}")
        else:
            print("Username not found.")

    elif choice == '3':
        break