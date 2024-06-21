__package__ = "Backend"
from cryptography.fernet import Fernet


class keygen:
    key = None

    @classmethod
    def getkey(cls):
        if keygen.key is None:
            keygen.key = Fernet.generate_key()
            with open('Backend\\mykey.key', 'wb') as file:
                file.write(keygen.key)
            return keygen.key
        else:
            with open('Backend\\mykey.key', 'wb') as file:
                file.write(keygen.key)
            return keygen.key

            

            