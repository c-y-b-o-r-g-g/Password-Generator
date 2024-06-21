import os
import passgen
import Backend
from Backend import encryptor, decryptor


def save(site, password):
    decryptor.decrypt("passes.txt")
    with open("passes.txt", "a") as file:
        file.write(f"{site}: {password}\n")
    encryptor.encrypt("passes.txt")




l = int(input("Enter password Length: "))
password = passgen.generate(l)
print(password)

choice = str(input("Do you want to save? y/n"))
if choice == "y":
    site = str(input("Enter site: "))
    save(site, password)
