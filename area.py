
from turtle import circle

import shape_area

print("\n")

print("To find area of Circle")
r = float(input("Enter the Value of Radius : "))
print("The area of Circle is : ", shape_area.circle_area(r))

print("\n")

print("To find area of Triangle")
b = float(input("Enter the Value of Base : "))
h = float(input("Enter the Value of Height : "))
print("The area of Circle is : ", shape_area.triangular_area(b,h))

print("\n")

print("To find area of Rectangl")
l = float(input("Enter the Value of Length : "))
w = float(input("Enter the Value of Width : "))
print("The area of Circle is : ", shape_area.rectangular_area(l,w))
