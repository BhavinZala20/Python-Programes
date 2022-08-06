import numpy as np

from time import process_time_ns
from traceback import print_tb

'''
n1 = np.array([10,10,20,30])
print(type(n1))
print(n1)

print("\n")

n2 = np.array([[1,2,3], [4,5,6]])   # define array
print(n2)
print(n2.ndim)

print("\n")

n3 = np.zeros((3,3))    # it will form a 4X4 zero matrix
print(n3)

print("\n")

n4 = np.ones((3,3))     # it will print 3X3 array of all element 2
print(2*n4)

print("\n")

n5 = np.full((3,3),5)   # it will print all 5 elements in 3X3 matrix
print(n5)

print("\n")

n6 = np.arange(10,50,5)     # it will print 10 to 50 with the increment of 5 digits
print(n6)

print("\n")

n6 = np.arange(1,11)    # it will print 1 by 1 upto 10
print(n6)

print("\n")

n7 = np.random.randint(1,100,10)     # it will generate rndom value between 1 to 100 of noly 5 value
print(n7)

print("\n")

n8 = np.random.random(5)    # it will print float values
print(n8)

print("\n")

n9 = np.array([[1,2,3], [3,4,5], [4,5,6]])  # it will print the dimension of  given array
print(n9.shape)
print("\n")


n9.shape = (3,2)
n9.shape = (1,6)
print(n9.shape)


n10  = np.array([1,3,4,5])
n11  = np.array([6,8,9,2])

print(np.vstack((n10, n11)))    # it will print matrix in verticle format
print("\n")
print(np.hstack((n10, n11)))    # it will print matrix in horizontal format
print("\n")
print(np.column_stack((n10, n11)))  # it will print matrix in the form of stack 

print("\n")

print(np.sum([n10, n11]))    # it will print addition of two matrix
print("\n")
print(np.sum([n10, n11], axis = 0))    # it will do addition of coloum elements 
print("\n")
print(np.sum([n10, n11], axis = 1))    # it will do addition of row elements
print("\n")

print(n10 + 1)  # this 4 operations are very use in image processing
print(n10*2)
print(n10 - 2)
print(n10 / 2) # list DS will acccept every element for operations

print("\n")

a = np.ones((3,3))  
b = np.ones((3,3)) 
 
print((2*a) +(3*b))

print("\n")



# 1/08/2022 Lab-10

n = np.ones((3,3))
print(n)

d = np.eye(2)
print(d)

e = np.random.random((2,2))
print(e)

print("\n")

a = np.array([[1,2], [3,4]])
print(type(a))
print(a.shape)
# print(a[0], a[1], a[2])
# a[0] = 5
print(a)

print("\n")

b = np.array([[1,2,3], [4,5,6]])
print(b.shape)
print(b[0,0], b[0,1], b[1,0])

v = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(v)
b = v[:2, 1:3]
print(b)

print("\n")

print(v[0,1])
b[0,0] = 77
print(v[0,1])

print("\n")

row_r1 = v[1, :]
row_r2 = v[1:2, :]

print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
col_r1 = v[:, 1]
col_r2 = v[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)
'''


# 5/08/2022  Lab-11

# Array Math
x = np.array([[1,2], [3,4]], dtype=np.float64)
y = np.array([[5,6], [7,8]], dtype=np.float64)

print(x+y)
print(np.add(x,y))

print("\n")

print(x-y)
print(np.subtract(x,y))

print("\n")

print(x*y)
print(np.multiply(x,y))

print("\n")

print(x/y)
print(np.divide(x,y))

print("\n")

print(np.sqrt(x))

print("\n")

# dot function
v = np.array([9, 10])
w = np.array([11, 12])

print(v.dot(w))     # it will perform dot(.) operation
print(np.dot(v,w))

# transpose function

x = np.array([[1,2], [3,4]], dtype=np.float64)
y = np.array([[5,6], [7,8]], dtype=np.float64)

print(x)
print(x.T)

print("\n")
print(np.linspace(0,10,12))
print(np.arange(0,100,5))

print("\n")
f = np.array([1,2,3,4,5,7])
print(np.mean(f))
print(np.median(f))
print(np.std(f))

print("\n")
# Numpy Exopnentiation
A = np.arange(1,10)
print(A**2)
