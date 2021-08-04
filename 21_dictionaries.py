# import some functions and classes [doesn't work if filenames start w/ numbers eg. 98_test]
# explicitly calling '__import__' builtin might help # strhx = __import__('98_test')
from modules import strhx, now, nowf
import hashlib

print('\n>>> import strhx(), now() from file "modules"\n>>> from modules import strhx, now')
print('>>> now():', type(now))
print('>>> strhx():',type(strhx))
print('>>> strhx.__doc__: ',strhx.__doc__,sep='')

# associative array or map = dictionary (json like key:value pairs) in python

post_plain = {'user_id':209,'message':'hex representated message','language':'English','datetime':'20210804T134904Z','location':(44.590533, -104.715556)}
post_hex = {'user_id':209,'message':strhx('hex representated message'),'language':'English','datetime':'20210804T134904Z','location':(44.590533, -104.715556)}
all_hex = strhx(str(post_hex))

print('''\n>>> display items(key:value pair) in dictionary
print(post_plain.items())\n''', post_plain.items(), sep='\n')

print('''\n>>> display available keys in dictionary using post_plain.keys()
print(post_plain.keys())\n''', post_plain.keys(), sep='\n')

print('''\n>>> display specific key value in dictionary using post_plain.get('key')
print(post_plain.get('location'))\n''', post_plain.get('location'), sep='\n')

print('''\n>>> display specific key value in dictionary using post_plain['keyname']
print(post_plain['location'])\n''', post_plain['location'],sep='\n')

# access keys using index w/ additional list (unsure if this is a good or a bad idea, maybe the latter)
post_plain_index = list(post_plain.keys())
print('''\n>>> indirectly access dict items using index[1] but requires to create an additional list
>>> index is only available using this list, not the plain dict !
post_plain_index = list(post_plain.keys())''', sep='\n')
print(post_plain.keys(), '\nprint(post_plain_index[0]): ', post_plain_index[0], sep='')

# create hash objects for user_id value
print('''\n>>> create utf-8 encoded hash object 'post_plain_hash' for user_id
>>> post_plain_hash = hashlib.sha256(str(post_plain['user_id']).encode('utf-8'))''')
post_plain_hash = hashlib.sha256(str(post_plain['user_id']).encode('utf-8'))
print('post_plain_hash: ', post_plain_hash, 'type: ', type(post_plain_hash))

# create digest / hex representation of hash object
print('''\n>>> create hex representation of hash object 'post_plain_hash'
>>> post_plain_digest = post_plain_hash.hexdigest()''')
post_plain_digest = post_plain_hash.hexdigest()
print('post_plain_digest: ', post_plain_digest, '\ntype: ', type(post_plain_digest))

# add additional key:value pairs to dict
print('''\n>>> add new key 'hash' with sha256 value of 'user_id' (post_plain_digest) to dict post_plain''')
print('''post_plain['hash'] = post_plain_digest''')
post_plain['hash'] = post_plain_digest
print(post_plain)

# update value for key in dict from dict2 post_plain_update w/ same key
print('''\n>>> update value in post_plain['location'] using post_plain.update() method and
>>> 2nd dictionary 'post_plain_update' as input''')
post_plain_update = {'location':(94.590533, -24.715556)}
print('''dict2: post_plain_update = {'location':(94.590533, -24.715556)}''')
print('''post_plain key ['location']:''', post_plain['location'])
print('''post_plain_update key ['location']:''', post_plain_update['location'])
print('\npost_plain.update(post_plain_update), post_hex.update(post_plain_update)')
post_plain.update(post_plain_update)
post_hex.update(post_plain_update)
print('''\npost_plain, post_hex updated keys ['location']:''', post_plain['location'], post_hex['location'], '\nnow both match post_plain_update', sep='\n')

# hex conversion / compare
print('\nuse imported strhx function for message conversion to hex string')
print('\npost_plain:',post_plain,sep='\n')
print(type(post_plain))
print('\npost_hex:',post_hex,sep='\n')
print(type(post_hex))
# print('\nall_hex (whole dictionary):',all_hex,sep='\n')
# print(type(all_hex))

# arbitrary value for compare test
hx = '7b27757365725f6964273a203230392c20276d657373616765273a20273638363537383230373236353730373236353733363536653734363137343635363432303664363537333733363136373635277d'
hx_db = '68657820726570726573656e7461746564206d657373616765'

print('\nhx_db:',hx_db)
print('\npost_hex.get(\'message\'):',post_hex.get('message'))

if post_hex.get('message') == hx_db:
    print('\n>>> VALUE MATCH')
else:
    print('\n>>> VALUE NO_MATCH')

if all_hex == hx:
    print('\ninput:',all_hex,'\ndb:',hx,'\n>>> MATCH',sep='\n')
else:
    print('\ninput:',all_hex,'\ndb:',hx,'\n>>> NO_MATCH',sep='\n')

print('\nfinished:', now, nowf, '\n')
