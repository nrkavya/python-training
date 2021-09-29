'''Write a program (function!) that takes a list and returns a new list that contains all the elements
of the first list minus all the duplicates.'''

import time
Birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

print("Welcome to the birthday dictionary. We know the birthdays of: ")
time.sleep(1)
for x in Birthdays:
        print(x)


choice = input("Who's birthday do you want to look up? ")

if choice in Birthdays:
        print("{} birthday is: " .format(choice))
        print(Birthdays[choice])




