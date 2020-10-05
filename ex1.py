tup1 = (10)
print(type(tup1))

tup2= (10,)
print(type(tup2))

tup3 = (1,2,3,4)

a,b,c,d = tup3

print(a)

print(b)
print(c)

a =(1,2)
b = (1,1)

if a > b:
    print("a")
elif a==b:
    print("c")
else:
    print("b")

a = {"x":100, "y":200}

b = list(a.items())

print(b)


for index, elem in enumerate(b):
    print(index, elem)

list1 = ["a", "b", "c"]

for index, elem in enumerate(list1):
    print(index, elem)


for index, elem in enumerate(tup3):
    print(index, elem)


