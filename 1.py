#Create a program to compare three numbers and find the bigger numbers

no1 = int(input("Enter no1"))
no2= int(input ("Enter no2"))
no3 = int(input("enter no3"))

if(no1>no2 and no1>no3):
    print("no1 is greatest")
elif(no2>no1 and no2>no3):
    print("no2 is greatest")
else:
    print("no3 is greatest")
