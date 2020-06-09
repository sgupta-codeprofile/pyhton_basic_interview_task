# Task 1

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

def findFirstLast(getList):
    if type(getList) is list:
        if len(getList) != 0 and len(getList) != 1:
            return [getList[0],getList[-1]]
        else:
            return "Empty List or may be list contain one element"
    else:
        return "Plase pass the list only"


print(findFirstLast([5, 10, 15, 20, 25]))

