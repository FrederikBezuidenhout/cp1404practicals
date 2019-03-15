"""
Password checker and concealer.

Frederik Bezuidenhout
"""


MIN_LENGTH = 5

print("Enter a password that is at least {} characters long".format(MIN_LENGTH))
password = input(">")
while len(password) < MIN_LENGTH:
    print("Invalid Password. Try again")
    password = input(">")

concealed_password = len(password) * "*"

print(concealed_password)
