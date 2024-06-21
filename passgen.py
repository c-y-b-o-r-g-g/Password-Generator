import string
import random
letters = []

for i in range(len(string.ascii_letters)):
    letters += string.ascii_letters[i]
letters += 1,2,3,4,5,6,7,8,9,0
l = len(letters)
def generate(length):
    password = ""
    for i in range(length):
        x = random.randint(0,l-1)
        password+= str(letters[x])
    return password
