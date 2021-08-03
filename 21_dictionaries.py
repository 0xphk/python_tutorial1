# import some functions and classes [doesn't work if filenames start w/ numbers eg. 98_test]
# explicitly calling '__import__' builtin might help # strhx = __import__('98_test')
from modules import strhx, now

print('\n>>> import strhx(), now() from file "modules"\n>>> from modules import strhx, now')
print('>>> now():', type(now))
print('>>> strhx():',type(strhx))
print('>>> strhx.__doc__: ',strhx.__doc__,sep='')

# associative array or map = dictionary (json like key:value pairs) in python
print('\nuse imported strhx function for message conversion to hex string')
post_plain = {'user_id':209,'message':'hex representated message'}
post_hex = {'user_id':209,'message':strhx('hex representated message')}
all_hex = strhx(str(post_hex))
# print(strhx('phk'))
# print(strhx(str(post)))

print('\npost_plain:',post_plain,sep='\n')
print(type(post_plain))
print('\npost_hex:',post_hex,sep='\n')
print(type(post_hex))
print('\nall_hex (whole dictionary):',all_hex,sep='\n')
print(type(all_hex))

hx = '7b27757365725f6964273a203230392c20276d657373616765273a20273638363537383230373236353730373236353733363536653734363137343635363432303664363537333733363136373635277d'

if all_hex == hx:
    print('\ninput:',all_hex,'\ndb:',hx,'\n>>> MATCH',sep='\n')
else:
    print('input:',all_hex,'db:',hx,'\n>>> NO_MATCH',sep='\n')

print('\nfinished:', now, '\n')
