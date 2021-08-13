# python indentation conventions
# size of indentation doesn't matter, but has to be the same
# you could use 2, 4, or 8 chars (should be multiple of 4 flak8E111)

# assign var line must not be intended
print("""
name1 = 'John'
    name2 = 'sarah'
^___^ this is indented but not expected

print(name1,name2)
>>> IndentationError: unexpected indent
""")

# in conditions / loops / methods / functions etc.
# indentation is used to determine related fragments of codeblocks
print("""
i = 10
if i < 10:
print('smaller')
^
>>> IndentationError: expected an indented block

# correct ibndentation identifies following fragment correctly
if i < 10:
    print('smaller)
""")

# 6 chars as indent should not be used
print("""this works, but the linter will complain about E111
i = 1
while i < 10:
      i += 1
      print(i)
^__6__^ not a multiple of 4
""")
