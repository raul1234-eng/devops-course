a = {1: 11, 2: 23}

b = a.copy()
b.update({3:35})

del b[2]

print(list(b.keys()))

print(len(b))

c = {**a, **b}

print(c)

print(1 in c)
c.update({"1": 15})

print(c)

a.clear()
print(a)

del c[1]

print(c)

del b

#print(b)

c.pop(2)
c[10] = 100
print(c)
