#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.



name = str(input("enter your name: "))
age = int(input("enter your age: "))
year = str((2021 - age)+100)
print(name + " will be 100 years old in the year " + year)
