"""
Password checker and concealer.

Frederik Bezuidenhout
"""


MIN_LENGTH = 5


def main():
    password = get_password()
    conceal_password(password)


def get_password():
    print("Enter a password that is at least {} characters long".format(MIN_LENGTH))
    password = input(">")

    while len(password) < MIN_LENGTH:
        print("Invalid Password. Try again")
        password = input(">")

    return password


def conceal_password(password):
    concealed_password = len(password) * "*"
    print(concealed_password)


main()
