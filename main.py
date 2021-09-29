'''print("hello")
def add(*data):
    sum=0
    for d in data:
        sum = sum+d
    return sum

print(add(100,5,4,6,7))'''

'''#Accessing string characters in Python
str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])'''

'''# Python String Operations
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)'''


''''# Iterating through a string
count = 0
word = str(input("enter the word"))
for letter in word:
    if(letter == 'l'):
        count += 1
print(count,'letters found')'''

print("This is \x61 \ngood example")

print(r"This is \x61 \ngood example")


'''# Python string format() method

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)'''

"PrOgRaMiZ".lower()

"PrOgRaMiZ".upper()

"This will split all words into a list".split()

' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])

'Happy New Year'.find('ew')

'Happy New Year'.replace('Happy','Brilliant')


