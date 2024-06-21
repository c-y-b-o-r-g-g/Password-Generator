import string
import random

l = len(string.printable)
def generate(length):
    password = ""
    for i in range(length):
        x = random.randint(0,l-2)
        password+= str(string.printable[x])
    return password

