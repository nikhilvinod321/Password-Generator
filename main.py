import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print("Generated Password:", password)
