from sys import float_info

def tem_abs(a):
    if a<0:
        a = a*(-1)
        return ((a*1.8) + 32)

def temp_conv(a):
    
    if a<0:
        return  tem_abs(a) 

    else:
        return ((a*1.8) + 32)
    
a = float(input("Enter the Temprature Value (C) : "))
c = temp_conv(a)
print("The Value in Fahrenheit is :",c)


# lambda is a keyword in python
# Temprarure conversion using lambda keyword
x = lambda a : (a*1.8)+32   # ** is a represent the power  
print(x(a))

   