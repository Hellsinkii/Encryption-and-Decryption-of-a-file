# Create-File-Encryption-and-Decryption-Tool-with-Python


“Encryption is the most effective way to achieve data security. To read an encrypted file, you must have access to a secret key or password that enables you to decrypt it.” — Bruce Schneier

We'll walk you through the steps of creating a file encryptor and decryptor in python in this video. Even if you are unfamiliar with programming, you will be capable of adhering along since we will break down every code line and describe what it does. You'll have full-functioning encryption as well as a decryption tool by the end of this video that can be used to secure your documents from prying eyes. then let's get going!

Prerequisites
Make sure the following software is installed on your computer before we begin:

cryptography package 
Python 3

Getting Started
The requirement for this Python project can be installed using commands:
1.	Cryptography – pip install cryptography

Generating a Key
To encrypt and decrypt files, we need to generate a key that will be used to encrypt and decrypt the data. To generate the key, we will use the Fernet class from the cryptography package.
The generate_key() function generates a key and saves it to a file named secret.key. We are using the with statement to ensure that the file is properly closed after the key is written.

Loading the Key
Now that we have generated the key, we need to load it to use it for encryption and decryption.
The load_key() function opens the secret.key file and returns its contents.

Encrypting the File
The encrypt() function takes two parameters: the filename of the file to encrypt and the key used to encrypt it. First, we create a Fernet object with the key. Then, we open the file in binary mode and read its contents. We then use the encrypt() method of the Fernet object to encrypt the file data. Finally, we write the encrypted data back to the same file.

Decrypting a File
To decrypt a file, we need to load the key from the secret.key file and use it to decrypt the contents of the encrypted file.
The decrypt() function takes two arguments: the filename of the encrypted file and the key to decrypt it. First, we create a Fernet object using the key. Then, we open the encrypted file in binary mode and read its contents. We then use the decrypt() method of the Fernet object to decrypt the contents of the file. If the key is invalid or the file has been tampered with, we catch the InvalidToken exception and print an error message. Otherwise, we write the decrypted contents to the same file.

Putting it All Together
Now that we have implemented the generate_key(), load_key(), encrypt(), and decrypt() functions, we can use them to encrypt and decrypt files. We first ask the user whether they want to encrypt or decrypt a file, and then prompt them for the filename. We then call the appropriate function based on the user's choice.
We first ask the user for their choice and convert it to lowercase. If the user chooses to encrypt a file, we prompt them for the filename and check if the file exists. If it does, we generate a key, load the key, and encrypt the file. If the user chooses to decrypt a file, we prompt them for the filename and check if the file exists. If it does, we load the key and decrypt the file. If the user enters an invalid choice, we print an error message.

