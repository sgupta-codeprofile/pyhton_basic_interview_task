# Task 10


# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Example:
# If the following email address is given as input to the program:

# akita@example.com

# Then, the output of the program should be:

# example

# In case of input data being supplied to the question, it should be assumed to be a console input.
import re

def searchCompany(email = None):
    if email is None:
        return "Please pass email"
    emailValidation = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(emailValidation, email)):
        filterEmail = email.split('@')
        filterEmail = filterEmail[1].split('.')[0]
        return filterEmail
    else:
        return "Invalid Email"


if __name__ == "__main__":
    result = searchCompany('akit@example.com')
    print(result)


