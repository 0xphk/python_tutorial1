# booleans True False
print('a = 3')
print('b = 5')
a = 3
b = 5
print("a == b", a == b, type(a == b))

print("a < b", a < b, type(a < b))

print("a > b", a > b, type(a > b))

print("a != b", a != b, type(a != b))

print("\nconvert number to bool")
print("bool(28)", bool(28), type(bool(28)))
print("bool(3.145)", bool(3.145), type(bool(3.145)))
print("bool(-2.71828)", bool(-2.71828), type(bool(-2.71828)))
print("bool(0)", bool(0), type(bool(0)), 'zero return False')

print("\nconvert string to bool")
print('bool("Turing")', bool("Turing"), type(bool("Turing")))
print('bool(" ")', bool(" "), type(bool(" ")))
print('bool("")', bool(""), type(bool("")), 'empty string return False')

print("\nconvert bool to string")
print('str(True)', str(True), type(str(True)))
print('str(False)', str(False), type(str(False)))

print("\nconvert bool to int")
print('int(True)', int(True), type(int(True)))
print('int(False)', int(False), type(int(False)))

print("\narithmetic with bool and int, converts bool to int first, then adds")
print('5 + True', 5 + True, type(5 + True))
print('10 * False', 10 * False, type(10 * False))
