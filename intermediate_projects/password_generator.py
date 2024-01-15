import string
import random

print("\t Welcome to password generator !!!")
chars = list(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits)

number = int(input("Input ammount of passwords to generate: "))
length = int(input("Input your password lenght: "))
print("\nHere are your passwords: ")


for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)

    print(password)

# def random_pass(n, l):
#     for pwd in range(n):
#         password = ''
#         for c in range(l):
#             password += random.choice(chars)
#         print(password)
#
#
# random_pass(number, length)
