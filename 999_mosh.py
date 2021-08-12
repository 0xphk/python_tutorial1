# mosh [https://www.youtube.com/watch?v=kqtD5dpn9C8]
from modules import color, term_reset, spinit
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
print('reset term in 2s ...',end=' ',sep='')
print(color.DARKCYAN)
#sleep(5)
spinit(5)
print(color.END)
term_reset()

# calculate w/ different datatypesphk
print(color.BOLD,color.DARKCYAN,"Python for Beginners by mosh - Calculation of different datatypes",color.END,sep='',end='\n')
First = 10.1
Second = 20
Sum = First + float(Second)
print('First:\t',First,'\t',type(First),'\nSecond:\t',Second,'\t',type(Second),'\nSum:\t',Sum,'\t',type(Sum))
print('reset term in 3s ...',end=' ',sep='')
print(color.DARKCYAN)
spinit(10)
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
print('reset term in 3s ...',end=' ',sep='')
print(color.DARKCYAN)
spinit(10)
print(color.END)
term_reset()


# arithmetic operators
print(color.BOLD,color.DARKCYAN,"Python for Beginners by mosh - Arithmetic operators",color.END,sep='',end='\n')
print('Arithmetic operators:')
print('Addition: 10 + 3 = ',10 + 3)
print('Substraction: 10 - 3 = ',10 - 3)
print('Multiplication: 10 * 3 = ',10 * 3)
print('Exponent x^n: 10 ** 3 = ',10 ** 3)
print('Division(float): 10 / 3 = ',10 / 3)
print('Division(int): 10 // 3 = ',10 // 3)
print('Division(remainder): 10 % 3 = ',10 % 3)
