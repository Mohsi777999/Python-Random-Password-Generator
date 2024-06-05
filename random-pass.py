import random
import string

pass_len = 12
characters = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(characters)

print("Your Random Password is", password)
