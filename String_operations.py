from dataclasses import replace
from posixpath import split


a = "IICT"
print(a.find('C'))  # index always strats with 0
print(a.count('I'))

print(len(a))   # in python lenght always starts with 1

print(a.upper())

print(a.lower())

print(split(a))

print(a.replace('I','A'))

Fruit = "Bananas, apples, mangoes"
print(Fruit.split(','))


# String Operations
'''
len()
lower()
upper()
split()
replace()
find()
count()
'''

# reverse a string
a = "Bhavin"[: :-1] # It is strat from 0
print(a)

# to write python code replace a = "My Department Name is ICT, My Name is Bhavin"
# Output : "My department name is ICT, apples, mangoes, My name is Bhavin"

a = "My Department Name is ICT, My Name is Bhavin"
print(a)

print(a.replace('D','d'))



