'''
1) Tuple
2) List
3) Dictionary
4) Set

'''
# 1) tup data strcture is Mutable

import this


tup1 = (1, "a", True, 2+3j)     # it is start from 0 (index)
print(type(tup1))

'''

            tuple = (1,"a",True,2+3j)
            print(type(tuple))

            1  ,  "a"  ,  True  ,  2+3j
    Index   0      1        2        3  {Positive}
    Index  -4     -3       -2       -1  {Negative}

'''

print(tup1[0])
print(tup1[1])
print(tup1[2:4])

print("\n")

print(tup1[-1])     # last element starts with 0
print(tup1[-2])
print(tup1[-4:-2])

tup1 = (1,2,3)
tup2 = (4,5,6)

print(tup1[::-1])
print(tup2[::-1])

print(tup1 + tup2)
print(tup2 + tup1)

print(tup1*2)
print(tup2*2)

tup1 = ("ICT", 300)
tup2 = (1,2,3)
print((2*tup1 + tup2))

# 2) List data structure is Immutable

l1 = [1,"a", True, 4]
print(type(l1))

l1[0] = 100
print(l1[0])
print(l1[1:4])
print(l1[-1])

print("\n")
print("\n")


# 15/07/2022
# 3) Dictionary Data structure and this is mutable
# Dictionary is a unordered collection of elements in keys and values pairs and closed with {}

d1 = {"Apple":20, "Mango":30}
print(type(d1))

print(d1.keys())
print(d1.values())

d1["Apple"] = 100
d1["Mango"] = 200
print(d1)           # that's why the dictionary data structure is mutable

d2 = {"Banana":30, "Orange":60}
d1.update(d2)       # for concate
print(d1)

d2["Ice Creme"] = 50
d1.update(d2)
print(d1)

d2.pop("Orange")    # to remove perticular element
print(d2)

#d1.sort()
print("\n")
print("\n")


# 4) Set data structure 
# set is a unordered and unindex collection of element and closed with {}
# this output will generate randomly and it is mutable

s1 = {1, "Bhavin", 3+2j}
#s2 = {"Mahadev", 1, 2+3j}
print(type(s1))
#print(type(s2))

s1.add("Abhishek")
print(s1)

s1.update([1,2,3])
print(s1)

s1.remove("Bhavin")
print(s1)

s1 = {4,5,6,7}
s2 = {1,2,3,4}
print(s1.union(s2))
print(s1.intersection(s2))


