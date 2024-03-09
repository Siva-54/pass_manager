# Password Encryption and Decryption Script

This Python script allows you to encrypt and decrypt passwords using the Fernet encryption algorithm and store them securely.

## Prerequisites

- Python 3
- [cryptography](https://pypi.org/project/cryptography/) library

You can install the required library using pip:

```bash
pip install cryptography
```

## Usage

1. **Generate Key**: Run the script to generate a key file (`key.key`) required for encryption and decryption. If the key file already exists, this step is skipped.

2. **Encrypt and Save Password**: Choose option 1 to enter a username and password. The password will be encrypted using the generated key and saved to the `user_data.txt` file.

3. **Decrypt Password**: Choose option 2 to enter a username. The script will retrieve the corresponding encrypted password from the `user_data.txt` file, decrypt it using the key, and display the decrypted password.

4. **Exit**: Choose option 3 to exit the script.

## File Descriptions

- `password_encrypt_decrypt.py`: The main Python script containing functions for generating, loading, encrypting, and decrypting passwords.
- `key.key`: The key file required for encryption and decryption.
- `user_data.txt`: The file where encrypted usernames and passwords are stored.

## Important Notes

- Ensure that you keep the `key.key` file secure. Without it, you won't be able to decrypt the passwords.
- The script uses Fernet encryption, which provides secure encryption and decryption of passwords. However, it's essential to follow best practices for password management and storage.

## Contributors

- [Siva Shankar Reddy](https://github.com/siva-54)

## License

This project is licensed under the [MIT License](LICENSE).
