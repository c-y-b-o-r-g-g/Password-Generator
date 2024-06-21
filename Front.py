import os
import Backend.passgen as passgen
import Backend
from Backend import encryptor, decryptor


def save(site, password):
    decryptor.decrypt("passes.txt")
    with open("passes.txt", "a") as file:
        file.write(f"{site}: {password}\n")
    encryptor.encrypt("passes.txt")

l = input("Enter password Length: ")
l = int(l) if l.isdigit() else 0
if not isinstance(l, int) or l <= 0:
    print("Invalid password length. Please enter a positive integer.")
else:
    password = passgen.generate(l)
    print(password)

    choice = str(input("Do you want to save? y/n"))
    if choice == "y":
        site = str(input("Enter site: "))
        if len(site) == 0:
            print("Invalid site name. Please enter a non-empty string.")
        else:
            save(site, password)

    view_choice = str(input("Do you want to view saved passwords? y/n"))
    if view_choice == "y":
        decryptor.decrypt("passes.txt")
        with open("passes.txt", "r") as file:
            saved_passwords = file.readlines()
            for line in saved_passwords:
                print(line.strip())
        encryptor.encrypt("passes.txt")


