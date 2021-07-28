print("# range iteration as function")
def iterate():
    for i in range(1, 10):
        print(i)

iterate()

print("age verify as function")
def compare_age():
    age = int(input("enter age: "))
    if age == 18:
        print("age is 18!")
    elif (age < 21) and (age > 18):
        print("age over 18 but not yet 21!")
    elif age == 21:
        print("age is 21!")
    elif age > 21:
        print("age over 21!")
    else:
        print("age under 18!")
compare_age()

# parameters to functions
print('use function parameter "name"')
def hello(name):
    print("hello", name)
hello("phk")

print(hello("name_here"))
print(type(hello("name_here")))

# variables as parameters to functions
print('use variables as function parameter "name", "age"')
name = str(input("enter name: "))
age = int(input("enter age: "))
def hello(name, age):
    print("name, age:", name,",", age)
    #return age
hello(name, age)

# determine max value from inputs
print("\n# max value function")
a = int(input("value1: "))
b = int(input("value2: "))
def max(a, b):
    if a < b:
        return b
    else:
        return a
result = max(a, b)
print("max value:",result)