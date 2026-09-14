# Write a Python function that takes an email address as input and uses a regular
# expression to validate if it is a valid email address. The function should return True for
# valid emails and False for invalid ones.

import re


def validate_email(email):
    
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False

        
email = input("Enter email address: ")

# Validate email
if validate_email(email):
    print("Valid Email")
else:
    print("Invalid Email")