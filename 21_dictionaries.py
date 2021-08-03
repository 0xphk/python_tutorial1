# import some functions and classes [doesn't work if filenames start w/ numbers eg. 98_test]
# explicitly calling '__import__' builtin might help # strhex = __import__('98_test')
from modules import strhex, now

print('>>> import strhex(), now() from file "modules"\n>>> from modules import strhex, now')
print('>>> now():', type(now))
print('>>> strhex():',type(strhex))
print('>>> strhex.__doc__: ',strhex.__doc__,sep='')

# associative array or map = dictionary (json like key:value pairs) in python
print('\nuse imported strhex function for message conversion to hex string')
post_plain = {'user_id':209,'message':'hex representated message'}
post_hex = {'user_id':209,'message':strhex('hex representated message')}

# print(strhex('phk'))
# print(strhex(str(post)))

print(post_plain)
print(post_hex)

print('\nfinished:', now, '\n')
