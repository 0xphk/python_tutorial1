# strings and literal strings
print("string")
print('literal_string?')
print('literal string containing "string"')
print('\'literal string\' containing "string"')

# print multiline strings using '''
print('''\'literal string\'
      in multi lines
      with "string"
      ''')

# combine strings using + operator (1 + 2 + 3 == 123)
print('combine ' + '\'literal strings\' ' + 'using + operator')

print('combine ' + 'strings')

# exploring string methods

# string.center(width: int, fill: str_char)
# fill strings left and right w/ unicode chars until width is reached
my_string = 'Just\tSome\tString'
x = my_string.center(40,'*')
print(my_string)
print(x)
print()

# define tab size
# fill tab character with whitespaces to n, do not count tab char
# so this should replace each \t with 5 whitespaces, n / tabs to reach 10 in total
#y = x.expandtabs(10)  # but this returns 6 whitespaces per tab, 5 expected
#print(y)

# strange results/output, maybe terminal/shell(urxvt) related
i = 0
while i < 10:
    i += 1
    y = x.expandtabs(i)
    print(i,y)

# format using positional args (again^^)
name = "Dude"
email = """
Hello {},
how are you?
"""
print(email.format(name))

# using fprint and directly calling name var
email = f"""
Hello {name},
how are you?
some calc {2 + 12}
some concat {name + str('2') + str(12)}
"""
print(email)

# print str repr of numbers in reverse order using [::-1]
# slice str starting at the end of the string and move backwards.
numbers = [1,2,3,4,5,7,6,8]
print(str(numbers)[::-1])

# if multiply operator is used on strings it turns to string replication operator
print(name * 5)
