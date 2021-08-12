# mosh [https://www.youtube.com/watch?v=kqtD5dpn9C8]

# vars 5-9m
name = " John Smith"
age = 20
new_patient = True

# input ~9-19m
name = input('name: ')
print('>>> w/o strip(): hello ',name)
# strip() whitespaces from string
print('>>> w/ strip(): hello '.strip(),name)

birth_year = input('birth_year?:\t')
birth_month = input('birth_month?:\t')
current_year = 2021
current_month = 8
age = 2021 - int(birth_year)
if int(birth_month) < int(current_month):
    age += 1
print('you are currently: ',str(age).strip(),'years old!')

First = 10.1
Second = 20
Sum = First + float(Second)
print('First:\t',First,'\t',type(First),'\nSecond:\t',Second,'\t',type(Second),'\nSum:\t',Sum,'\t',type(Sum))
