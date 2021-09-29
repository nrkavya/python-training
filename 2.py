#Write the above solution in a function which takes take numbers and return the bigger number


n1 = int(input("enter n1: "))
n2 = int(input("enter n2: "))
n3 = int(input("enter n3: "))

def biggest(n1,n2,n3):
    if(n1>n2) and (n1>n3):
        return n1
    elif (n2>n3) and (n2>n1):
        return n2
    else:
        return n3

print(biggest(n1,n2,n3))