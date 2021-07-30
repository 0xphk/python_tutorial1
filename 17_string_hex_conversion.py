# string to hex conversion and vice versa using different methods
import codecs

# format output
print("\nformatted output from input, hex+byte conversion of strings\n")
name = input("enter name: ")
# {n} references n positional argument
print('''\n>>> print("hello {0}".format(name)) is the same as print("hello {}".format(name)
>>> {}  implicitly references the first positional argument format(name)
>>> {0} explicitly references the first positional argument format(name)\n''')
print("hello {}".format(name))
print()

# 2nd postitional arg does not yet exist so this fails
# print("hello {1}".format(name))

# convert input string to hex representation
name_hex = name.encode('utf-8').hex()
print("hex representation of string 'name' as hex string 'name_hex':", repr(name.encode('utf-8').hex()))
print(">>> type of 'f{repr(name.encode('utf-8').hex()}':", type(repr(name.encode('utf-8').hex())))
print("\nhex encoding of string 'name' as hex string 'name_hex':", name.encode('utf-8').hex())
print(">>> type of 'f{name.encode('utf-8').hex()}':", type(name.encode('utf-8').hex()))

# add new arguments as first and third positional argument
print("\nput things together using '0x{2} {0}{1}{3}'.format('(', name, name_hex, ')')\n")
print('hello 0x{2} {0}{1}{3}'.format('(', name, name_hex, ')'))

#print('hello 0x{2} {0} {1} {4}'.format("(", name, name_hex, ")"))

# python3 can use bytearry to convert hex string back to ascii string
name_byte = bytearray.fromhex(name_hex)
print("\nconvert hex value back from bytearray ascii string to string:\n")
print('hello back {1} {0}0x{2}{3}'.format('(', name_byte.decode(), name_hex, ')'))
print("\n>>> type of: 'name_byte.decode()':", type(name_byte.decode()))
print()

# python3 can also use module function codecs.decode() to convert hex string back to ascii string
# use import codecs on top of file

name_bin = codecs.decode(name_hex, 'hex')
#name_bin2 = name_bin.strip(decode(name_hex, 'hex'))
print("convert hex value to binary_string:", name_bin)
print(">>> type of 'f{codecs.decode(name_hex, 'hex')}':", type(codecs.decode(name_hex, 'hex')))
print("\nconvert hex value back from binary_string to string:", str(name_bin, 'utf-8'))
print(">>> type of '{str(name_bin, 'utf-8')}':", type(str(name_bin, 'utf-8')))
print()
