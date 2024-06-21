__package__ = "Backend"

import cryptography
from cryptography.fernet import Fernet
import os

def decrypt(filename):
  try:
    with open("Backend\\mykey.key", "rb") as file:
        key = file.read()
    fernet = Fernet(key)
  except Exception as e:
    print(f"Error retrieving key: {e}")
    return

  with open(filename+".encrypted", 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()

  try:
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, 'wb') as decrypted_file:
      decrypted_file.write(decrypted_data)
  except cryptography.fernet.InvalidKey:
    print("Invalid decryption key. Please check your key manager.")

