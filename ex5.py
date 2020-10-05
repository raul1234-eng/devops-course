str1 = "abcde"

print(str1[2])

print(str1[1:3])

print("a" in str1)

print("b" not in str1)

print("ab" in str1)

print(r"ab\ncd\n//")

name = "unu"
number = 1

print("%s %d" %(name, number))

print("{} {}".format(name, number))

print("{1} {0}".format(number, name))

namenum = name + str(number)

print(namenum)

print(name * 2)

print(name[0:2] + name[1] * 2)

str2 = "I like Java"

str2 = str2.replace("Java", "Python")

print(str2)

print(str2.upper())

print(str2)

print(str2.lower())

print(str2.capitalize())

print(str2.title())

print(" ".join(str2))

print(''.join(reversed(str2)))
print(str2.split("l"))
str3 = "   abcde    "
print(str3.strip(), end ="")
print(1)
print(str3.lstrip(), end = "")
print(2)
print(str3.rstrip(), end= "")
print(3)
str1 = "ana are mere"
str_count = str1.count("a")
print("str_count", str_count, "test")
print(__name__)




