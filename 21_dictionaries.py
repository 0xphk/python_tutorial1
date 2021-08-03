# import some functions and classes [doesn't work if filenames start w/ numbers eg. 98_test]
# explicitly calling '__import__' builtin might help # strhex = __import__('98_test')
from modules import strhex, now

print('import strhex(), now() from file "modules"\nfrom modules import strhex, now\n')
print('now():', type(now))
print('strhex():', type(strhex))
print(strhex.__doc__)

# associative array or map = dictionary (json like key:value pairs) in python
# use imported strhex function for message conversion to hex string
post = {"user_id":209,"message":strhex('hex representated message')}

# print(strhex('phk'))
# print(strhex(str(post)))
print(post)

print('\nfinished:', now, '\n')
