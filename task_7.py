# Task 7

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import random

def passwordGenerator(strength = 12):
    stringForPass = "ACONITEYDATAsWithEDucationtySolution0123450shuBham!@&*()#$%^?"
    if strength == 'weak':
        return "".join(random.sample(stringForPass[0:10], 10))
    return "".join(random.sample(stringForPass, strength))

switcher = {
    1: passwordGenerator(), #strong
    2: passwordGenerator(15), #strongest
    3: passwordGenerator("weak"), #weak
}

def main():
    result = ''
    try:
        take_user_input = int(input("How strong password you want \n 1-Strong \n 2-Strongest \n 3-Weak \n"))
        result = switcher.get(take_user_input, "Wrong Choice")
    except ValueError:
        print("*************Please Enter Number only*************")
        take_user_input = None
        main()
    print(result)

if __name__ == "__main__":
    main()