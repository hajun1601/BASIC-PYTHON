a = [1, 2, 3, 4, 5]
b = a
c = [1, 2, 3, 4, 5]
print(a is b)
print(a is not b)
print(id(a))
print(id(b))
print(a is c)
print(a is not c)
print(id(a))
print(id(c))