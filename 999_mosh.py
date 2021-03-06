# coding w/ mosh: python in 1h [https://www.youtube.com/watch?v=kqtD5dpn9C8]
from modules import ansicolor, color, term_reset, spinit
from time import sleep

term_reset()
print(color.BOLD,color.DARKCYAN,"Python for Beginners by mosh - Inputs",color.END,sep='',end='\n')
sleep(1)
# vars ~5m - ~9m
name = " John Smith"
age = 20
new_patient = True
print('\nPatient name:\t',name.strip(),'\nPatient age:\t',str(age).strip(),'\nIs new patient?\t',str(new_patient).strip(),sep='',end='\n\n')

# input ~9m - ~19m
#name = input('name: ')
name = 'phk'
print('>>> w/o strip(): hello ',name)
# strip() whitespaces from string
print('>>> w/ strip(): hello '.strip(),name)

#birth_year = input('birth_year?:\t')
#birth_month = input('birth_month?:\t')
birth_year = 1977
birth_month = 7
current_year = 2021
current_month = 8
age = 2021 - int(birth_year)
if int(birth_month) < int(current_month):
    age += 1
print('you are currently: ',str(age).strip(),'years old!')
print('reset term in 1s ...',end=' ',sep='')
print(color.DARKCYAN)
spinit(4)
print(color.END)
term_reset()

# calculate w/ different datatypesphk
print(color.BOLD,color.DARKCYAN,"Python for Beginners by mosh - Calculation of different datatypes",color.END,sep='',end='\n')
First = 10.1
Second = 20
Sum = First + float(Second)
print('First:\t',First,'\t',type(First),'\nSecond:\t',Second,'\t',type(Second),'\nSum:\t',Sum,'\t',type(Sum))
print('reset term in 1s ...',end=' ',sep='')
print(color.DARKCYAN)
spinit(4)
print(color.END)
term_reset()

# strings ~19m - ~24m
print(color.BOLD,color.DARKCYAN,"Python for Beginners by mosh - Strings",color.END,sep='',end='\n')
course = "Python for Beginners"
print('course:',color.CYAN,course,color.END,end='\n')
print('using str.upper() method:',color.DARKCYAN,color.BOLD,course.upper(),color.END)

# find index of letter 'y'
print('find index of letter "y":',course.find('y'))
print('replace lowercase "ython" to uppercase:',course.replace('ython', 'YTHON'))

# check for parts of str(), return bool
print('is "Python" part of str(course):','Python' in course)
print('reset term in 1s ...',end=' ',sep='')
print(color.DARKCYAN)
spinit(4)
print(color.END)
term_reset()

# arithmetic operators
print(color.BOLD,color.DARKCYAN,"Python for Beginners by mosh - Arithmetic operators",color.END,sep='',end='\n')
print('''Arithmetic operators precedence: **,*,/,//,%,+,-''')
print('Addition: 10 + 3 = ',10 + 3)
print('Substraction: 10 - 3 = ',10 - 3)
print('Multiplication: 10 * 3 = ',10 * 3)
print('Exponent x^n: 10 ** 3 = ',10 ** 3)
print('Division(float): 10 / 3 = ',10 / 3)
print('Division(int): 10 // 3 = ',10 // 3)
print('Division(remainder): 10 % 3 = ',10 % 3)
print('reset term in 1s ...',end=' ',sep='')
print(color.DARKCYAN)
spinit(4)
print(color.END)
term_reset()

# logical operators
print(color.BOLD,color.DARKCYAN,"Python for Beginners by mosh - Logical operators",color.END,sep='',end='\n')
price = 25
print('\nprice is:',price)
print('is price >10 and <30? :',price > 10 and price < 30)
# same but shorter
print('is price < 30 > 10? :',price < 30 > 10)
print('reset term in 1s ...',end=' ',sep='')
print(color.DARKCYAN)
spinit(4)
print(color.END)
term_reset()

# convert weight from input
print(color.BOLD,color.DARKCYAN,"Python for Beginners by mosh - Weight conversion",color.END,sep='',end='\n')
# weight = int(input('\nenter weight :\t'))
# unit = input('(K)g or (L)bs :\t')
weight = 170
unit = "l"
if unit.upper() == "K":  # shorter instead of [if unit == "K" or unit == "k":]
    unit = "Kg"
    unit_conv = "Lbs"
    # better formatting by concatenate strings instead of [print('weight in Kg :\t',weight,unit)]
    print('weight in Kg :\t' + str(weight) + unit)
    weight_conv = weight / 0.45
    print('weight in Lbs :\t' + str(weight_conv) + unit_conv)
elif unit.upper() == "L":
    unit = "Lbs"
    unit_conv = "Kg"
    print('weight in Lbs :\t' + str(weight) + unit)
    weight_conv = weight * 0.45
    print('weight in Kg :\t' + str(weight_conv) + unit_conv)

if weight > 100 and unit == "Kg":
    print("maybe it's time for some diet...")
elif weight < 70 and unit == "Kg":
    print("you should eat something...")

print('reset term in 1s ...',end=' ',sep='')
print(color.DARKCYAN)
spinit(4)
print(color.END)
term_reset()
print(color.BOLD,color.DARKCYAN,"Python for Beginners by mosh - while loop, print expression",color.END,sep='',end='\n')
i = 1
# 1_000 provides better readable numbers
while i <= 10:
    # multiply i by str(), allows to print expression, increment count of str() on every iteration
    print(i * '*')
    i += 1
    sleep(0.1)

print('reset term in 1s ...',end=' ',sep='')
print(ansicolor.fg.lightcyan)
spinit(4)
print(ansicolor.reset)
term_reset()
