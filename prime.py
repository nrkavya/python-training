#prime number from 1 to 100

print("Prime numbers between 1 and 100 are:")
for num in range(1,100):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)