
from re import X


def dispaly():
    print("ICT")
    
dispaly()


def add(a,b):
    return a+b

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : ")) 
c = add(num1, num2)
print(c)



print("\n")


def prime():
    
    num = int(input("Enter the number : "))
    
    if(num == 0):
        print("Enter Non Zero Integer Value")
        a = prime()
        
    elif(num == 1):
        print("Enter Value in which 1 is not Include")
        a = prime()
        
    elif(num<0):
        num = num*(-1)
        a = prime()
    
    if(num>0):
        
        i = 2
        j=0
        
        while i<=num/2 : 
            if(num % i) == 0 :
                j=1
            break 
        i=i+1
        
        if j==0 :
            print(num,"is prime")
            print("Please Enter the Positive Number Next Time")
        else :
            print(num,"is not prime")
            print("Please Enter the Positive Number Next Time")
                
a = prime()


print("\n")

# for factorial 
def fact():
    
    num = int(input("Enter the number : "))
    
    if(num == 0):
        print("Factorial of 0 is : 1")
        
    elif(num == 1):
       print("Factorial of 1 is : 1")
        
    elif(num<0):
        print("Please Enter Positive Value : ")
        a = fact()
    
    else:
        fact1 = 1
        i = 1
        
        while i<=num :
            fact1 = fact1 * i
            i+=1
            print("Factorial of",num,"is",fact1)
            print("\n")
            
a = fact()
    

print("\n")

def max():
    num1 = int(input("Enter the number : "))
    num2 = int(input("Enter the number : "))

    if(num1>num2):
        print(num1, "is Max")
        
    else:
        print(num2, "is Max")
        
c=max();