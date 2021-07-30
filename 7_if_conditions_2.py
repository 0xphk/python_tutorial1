# string length input
print("# check string/number length of input")
string = input("\nenter string[8]: ")
if len(string) < 8:
    print("\nstring is too short\n8 characters minimum\n")

# number length input
print("# determine number length by converting it to string so len() could work\n")
number = int(input("enter digits[8]: "))
if len(str(number)) < 8:
    print("\nnumber too small\nenter at least 8 digits")
else:
    if number % 2 == 0:
        print("btw. even number\n")
    else:
        print("btw. odd number\n")

print("\n# fun with triangles\n")
print('''# scalene triangle - all sides different lengths
# isosceles triangle - two sides have same length
# equilateral triangle - all sides are equal''')

a = int(input("\nlength of a: "))
b = int(input("\nlength of b: "))
c = int(input("\nlength of c: "))

# shorter
if a != b and b != c and a != c:
    print("\nscalene triangle\n")
elif a == b == c:
    print("\nequilateral triangle\n")
else:
    # long elif (a == b and b != c) or (a == c and b != c) or (b == c and a != c):
    print("\nisosceles triangle\n")
