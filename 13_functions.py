# basic function with arguments

def greeter(name, age=-1):
    print(f'Hello {name}')
    if not age < 0:
        print(f'Age is: {age}')

greeter('John', 18)
greeter('James')

# return values from functions
def isAdult(age):
    if age >= 18:
        print('Adult:',end=' ')
        return True

print(isAdult(21))

# shorter but only return bool
def isAdult(age):
    return age >= 18

print(isAdult(21))

# return string after comparison
def isGender(gender='unknown'):
    if gender.upper() == "M":
        return 'Male'
    elif gender.upper() == "F":
        return "Female"
    else:
        return gender

print(isGender('m'))
print(isGender('f'))
print(isGender('x'))
