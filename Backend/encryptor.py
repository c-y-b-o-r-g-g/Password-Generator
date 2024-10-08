from cryptography.fernet import Fernet
from . import keymanager
import os

def encrypt(filename):
    key = keymanager.keygen.getkey()
    cipher = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()      
    encrypted = cipher.encrypt(data)
    with open(filename+".encrypted", "wb") as file:
        file.write(encrypted)
    os.remove(filename)
    
    