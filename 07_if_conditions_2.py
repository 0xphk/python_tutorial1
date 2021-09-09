# string length input
print("# check string/number length of input")
string = input("\nenter string[8]: ")
if len(string) < 8:
    print("\nstring is too short\n8 characters minimum\n")
else:
    print(len(string),'chars')

# number length input
print("# determine number length by converting it to string so len() could work\n")
number = int(input("enter digits[8]: "))
if len(str(number)) < 8:
    print("\nnumber too small\nenter at least 8 digits")
elif len(str(number)) >= 8:
    print(len(str(number)),'chars')
else:
    if number % 2 == 0:
        print("btw. even number\n")
    else:
        print("btw. odd number\n")

print("\n# fun with triangles\n")
print('''# scalene triangle - all sides different lengths
# isosceles triangle - two sides have same length
# equilateral triangle - all sides are equal''')

a = int(input("\nlength of a[1]: ") or 1)
b = int(input("\nlength of b[2]: ") or 2)
c = int(input("\nlength of c[3]: ") or 3)

# shorter
if a != b and b != c and a != c:
    print("\nscalene triangle\n")
elif a == b == c:
    print("\nequilateral triangle\n")
else:
    # long elif (a == b and b != c) or (a == c and b != c) or (b == c and a != c):
    print("\nisosceles triangle\n")

# ternary if conditions / statements
# some sort of inline condition, used in another exercise
# only if else, no elif in ternary if statements
number = 10

# simple if statement
if number > 0:
    print('positive')
else:
    print('negative')

# set var to empty value, all seems to work
number = None
number = False
number = int()
# check if var is not empty false if '' else true
if number:
    print('var is set and not empty')
else:
    print('var is set but empty')

number = 10
# ternary if statement, same as above but shorter, no elif
message = 'positive' if number > 0 else '0 or negative'
print(message)
