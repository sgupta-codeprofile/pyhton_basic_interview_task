# Task 6

# Write the Task 5 titles to the text file.

# Extras:
# Ask the user to specify the name of the output file that will be saved.

from task_5 import findTitle

fileName = input('Enter the file name--:')
fileName = fileName if len(fileName) > 0 else 'task_6'

with open(fileName + '.txt', 'w+') as saveFile:
    for title in findTitle():
        saveFile.writelines(title + '\n')