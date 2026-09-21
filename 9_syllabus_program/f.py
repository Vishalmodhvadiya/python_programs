# A website requires the users to input username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:
# • At least 1 letter between [a-z]
# • At least 1 number between [0-9]
# • 1. At least 1 letter between [A-Z]
# • At least 1 character from [$#@]
# • Minimum length of transaction password: 6

class User:
    def login(self, username, password):
        self.username = username
        self.password = password

        number = 0
        A_character = 0
        a_character = 0
        special_character = 0

        for ch in password:
            if ch.islower():
                a_character += 1
            elif ch.isupper():
                A_character += 1
            elif ch.isdigit():
                number += 1
            elif ch in "$#@":
                special_character += 1

        if len(password) >= 6 and len(password) <= 12:
           length = True
        else:
           length = False

        if A_character >= 1 and a_character >= 1 and number >= 1 and special_character >= 1 and length:
            print("Valid password")
        else:
            print("Invalid password")
            if length == False:
                print("- Password length must be between 6 and 12 characters")
            if A_character < 1:
                print("- Must contain at least 1 uppercase letter")
            if a_character < 1:
                print("- Must contain at least 1 lowercase letter")
            if number < 1:
                print("- Must contain at least 1 number")
            if special_character < 1:
                print("- Must contain at least 1 special character ($, #, @)")


user = User()
username = input("Enter username: ")
password = input("Enter password: ")
user.login(username, password)