# assignment operator =

value1 = 5
value2 = 5
#value2 /= 2     # value2 / 2
value2 += 5     # value2 + 5
#value2 -= 5
value3 = value1 + value2

print("assign values", value1, value2, value3)

# arithmetic operators
print("arithmetic operators + - * /")
print(1 + 2)
print(1 - 2)
print(1 / 2)
print(1 + 2 * 3)

# bool compare operators

print("check if 1 < 5")
print(1 < 5)
print(type(1 < 5))

print("check if 1 == 5")
print(1 == 5)
print(type(1 == 5))

print("check if 1 >= 5")
print(1 >= 5)
print(type(1 >= 5))

print("check if 1 != 5")
print(1 != 5)
print(type(1 != 5))

print("check combine (4 + 2) * 3 == 18")
print((4 + 2) * 3 == 18)
print(type((4 + 2) * 3 == 18))

# logic operators
print("age test")
age = int(input("age: "))

# same as 1st elif from 7_if_conditions.py
if (age < 21) and (age >= 18):
    print("age over 18 but not yet 21!!!")
elif (age < 18):
    print("sorry pal")
