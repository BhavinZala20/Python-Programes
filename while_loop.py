# While loop

i=1
while i<=10:
    print(i)
    i=i+1 # i+ = 1
    

print("\n")
print("\n")   
       

# To check your number is prime or not
 
i = 2
num = int(input("Enter the number : "))
j=0
while i<=num/2 : 
 if(num % i) == 0 :
    j=1
    break 
 i=i+1
 
if j==0 :
 print(num,"is prime")
else :
 print(num,"is not prime")
 
 
print("\n")


# Factorial

fact = 1
i = 1
num = int(input("Enter the number : "))
while i<=num :
 fact = fact * i
 i+=1
print("Factorial of",num,"is",fact)
print("\n")

'''
 There is 3 types of Control Statements:
 1) Continue
 2) Break
 3) Pass
'''
 
 
# 1) Continue Statement:

print("Continue Statement")
n=0
for n in range(20):
    if n == 1:
        continue
        print(n)
   
     
# 2) Break Statement:

print("Break Statement")
n=0
for n in range(10):
    if n == 5 :
        break
    print(n)
 

# 3) Pass Statement:

print("Pass Statement")
n=0
for n in range(10):
    if n == 5 :
        pass
        print(n)
