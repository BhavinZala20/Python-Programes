# String Operations

a = "My Department Name is ICT"
 
print(a[2:13])  # it will start after 2 characters and goes upto 13 digits
print(a[2:])    # it will skip 2 characters from the first and goes upto last
print(a[:12])   # it will print from first that means in +ve direction upto 12 characters
print(a[::1])   # it will print as it is
print(a[::-1])  # it will start from last (print reverse)
print(a[-8:-2]) # it will print from last to -8 digits and strat from before last 2 characters
print(a[::2])   # consider it will start at 1 if there is 2, if 3 then consider 2

a = " Bhavin "
print(a.strip()) # strip() = it will remove spaces(after & before)


# Conditional Statement
a=10
b=20

if a>b :
    print("a is grater than b")
    
elif a==b:
    print("a and b are Equal")
    
else :
    print("b is grater than a")


if 'a' in 'Bhavin':
    print("a is in bhavin")
    
elif 'a' not in 'Bhavin':
    print("a is not in Bhavin")
    
a=10
b="ICT "

if a%2==0 :
    print(2*b) 
else :
    print(b)