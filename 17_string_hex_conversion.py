# string to hex conversion and vice versa using different methods
import codecs

# format output
print("formatted output from input")
name = input("enter name: ")
# unsure why input is stored in {}
# {} Implicitly references the first positional argument {name}
# {0} references the first positional argument {name}
# print("hello {0}".format(name))
print('hello {}'.format(name))
print()

# 2nd postitional arg does not yet exist so this fails
# print("hello {1}".format(name))

# convert input string to hex representation
name_hex = name.encode('utf-8').hex()
print("hex representation of string 'name' as hex string 'name_hex':", repr(name.encode('utf-8').hex()))
print("type of 'f{repr(name.encode('utf-8').hex()}':", type(repr(name.encode('utf-8').hex())))
print("hex encoding of string 'name' as hex string 'name_hex':", name.encode('utf-8').hex())
print("type of 'f{name.encode('utf-8').hex()}':", type(name.encode('utf-8').hex()))

# add new arguments as first and third positional argument
print("\nput things together using format()")
print("hello id_0x{2} {0} {1}".format("name:", name, name_hex))

# python3 can use bytearry to convert hex string back to ascii string
name_byte = bytearray.fromhex(name_hex)
print("convert hex value back from bytearray ascii string to string:", name_byte.decode())
print("get type of: 'name_byte.decode()':", type(name_byte.decode()))
print()

# python3 can also use module function codecs.decode() to convert hex string back to ascii string
# use import codecs on top of file

name_bin = codecs.decode(name_hex, 'hex')
#name_bin2 = name_bin.strip(decode(name_hex, 'hex'))
print("get type of {name_bin}:", type(codecs.decode(name_hex, 'hex')))
print("convert hex value back from binary_string to string:", str(name_bin, 'utf-8'))
print("get type of 'name_bin':", type(str(name_bin, 'utf-8')))
