'''
1) for loop

'''


# check the number is prime or not
# for x in range(1,10):
from audioop import maxpp
from xml.dom import minicompat

min = 1
max = 100

print("Prime numbers between", min, "and", max, "are :")

for num in range(min, max + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           
           
# check the factorial

num = int(input("Enter a number: "))    # suppose user input 5
factorial = 1

if num == 0:
   print("The factorial of 0 is 1") 
else:
   for i in range(1, num + 1):      # (1, 6)
       factorial = factorial*i      # (1 = 1*120)
   print("The factorial of",num,"is",factorial)

