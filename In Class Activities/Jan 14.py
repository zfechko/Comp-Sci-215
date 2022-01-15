"""
Lecture concepts from January 14, 2022
Summary: Introduction to python operators and modifiers
"""

print("Hello world")

x = 11
y = 2
print("x =", x, "y =", y)

print(type(x)) # printing what data types x and y are
print(type(y))

z = x + y
print("z =", z)

z = x - y
print("z =", z)

z = x / y
print("z =", z)

z = x // y # divides but returns an integer rounded down
print("z =", z)

z = divmod(x, y) #divmod returns (x // y, x % y)
print(z)

"""
Moving on to strings
"""

a = "cpts"
b = "215"

print(a + '_' + b) #concatenating the strings
print(a[3]) #can index the string like an array
