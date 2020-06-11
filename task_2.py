# Task 2

# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

# My name is Michele

# Then I would see the string:

#  Michele is name My

# shown back to me.


# solution -:

def reverseString(getString):
    if type(getString) is str:
        if len(getString) != 0:
            newString = ' '.join(getString.split(' ')[::-1])
            return newString
        else:
            return "Empty string"
    else:
        return  "Plase pass the string"

print(reverseString("My name is Michele"))
