# Write a regular expression for checking if given email address is in correct form or not. Correct form is: usename @ domain prefix followed by top level domain. (Top level domains can be – com/edu/org. Username can contain +/./_/-)

import re

def valid_email(email):
    pattern = r'^[\w.+_-]+@[a-zA-Z0-9-]+\.(com|edu|org)$'
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("enter your email : ")
valid_email(email)
print(f"{email} -> {'Valid' if email else 'Invalid'}")