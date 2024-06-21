#Password Manager

## Overview

The Secure Password Manager is a comprehensive tool designed for generating, encrypting, and managing passwords securely. It integrates several modules, each responsible for a specific aspect of the password management process, including password generation, encryption/decryption, and secure storage.

## Modules

### Passgen

The [`passgen`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FSoftware%20Engineering%2FPython%20Projects%2FPassword%20Generator%2FBackend%2Fpassgen.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A0%2C%22character%22%3A0%7D%5D "Backend/passgen.py") module is responsible for generating secure passwords. It utilizes the following packages:

- **random**: To select random characters from ASCII characters, ensuring the uniqueness and security of each password.
- **string**: To access a variety of characters, including uppercase and lowercase letters, digits, and special characters, making the passwords complex and difficult to guess.

### KeyManager

The `KeyManager` module uses the `cryptography` package, specifically the `Fernet` class, to generate a secure encryption key. This key is crucial for the encryption and decryption of the password file. Key features include:

- **Singleton Design Pattern**: Ensures that the same encryption key is used across the application by implementing the `getkey` method. This method guarantees that the key is generated once and reused for both encryption and decryption processes.
- **Key Storage**: After generating the encryption key, it is stored in a file named `mykey.key`. This allows the application to retrieve the same key for the decryption process, ensuring data consistency and security.

### Encryptor

The [`encryptor`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FSoftware%20Engineering%2FPython%20Projects%2FPassword%20Generator%2FBackend%2Fencryptor.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A0%2C%22character%22%3A0%7D%5D "Backend/encryptor.py") module handles the encryption of password files. It operates as follows:

- **Encryption Process**: Utilizes the `Fernet` class from the `cryptography` package to encrypt password files. It retrieves the encryption key from the `KeyManager` module to ensure the use of a consistent key.
- **File Handling**: Encrypts the specified text file and renames it by appending `.encrypted` to the original filename (e.g., `original.txt` becomes `original.txt.encrypted`). After encryption, the original file is deleted to prevent unauthorized access, leaving only the encrypted version on the disk.

### Decryptor

The [`decryptor`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FSoftware%20Engineering%2FPython%20Projects%2FPassword%20Generator%2FBackend%2Fdecryptor.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A0%2C%22character%22%3A0%7D%5D "Backend/decryptor.py") module is tasked with decrypting previously encrypted password files. Its functionality includes:

- **Decryption Process**: Reads the encryption key from `mykey.key` and uses it to decrypt the encrypted file. This ensures that only files encrypted with the corresponding key can be decrypted successfully.
- **File Restoration**: After decryption, the data is stored in a new file with the original filename (e.g., `original.txt.encrypted` is converted back to `original.txt`), allowing for seamless access to the decrypted information.

## Main

The [`Main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FSoftware%20Engineering%2FPython%20Projects%2FPassword%20Generator%2FMain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\Software Engineering\Python Projects\Password Generator\Main.py") file serves as the entry point of the Secure Password Manager. It guides the user through the process of generating a password, saving it, and optionally viewing saved passwords. Key functionalities include:

- **Password Generation**: Prompts the user to enter the desired password length, then generates a secure password using the [`passgen`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FSoftware%20Engineering%2FPython%20Projects%2FPassword%20Generator%2FBackend%2Fpassgen.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A0%2C%22character%22%3A0%7D%5D "Backend/passgen.py") module.
- **Password Storage**: Offers the user the option to save the generated password, associating it with a specific website. The password is then encrypted and stored securely.
- **Password Retrieval**: Allows the user to view their saved passwords by decrypting the [`passes.txt.encrypted`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FSoftware%20Engineering%2FPython%20Projects%2FPassword%20Generator%2Fpasses.txt.encrypted%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\Software Engineering\Python Projects\Password Generator\passes.txt.encrypted") file, displaying the contents, and then re-encrypting the file for security.

## Security Measures

The Secure Password Manager prioritizes security at every step, from generating complex passwords to securely encrypting and storing them. By employing advanced encryption techniques and ensuring that the encryption key is securely managed and stored, it provides a robust defense against unauthorized access and cyber threats.

## Conclusion

The Secure Password Manager is an essential tool for anyone looking to enhance their online security. Its sophisticated encryption processes, coupled with an intuitive user interface, make managing passwords both secure and straightforward.