# python3 datastructure dictionaries: dicts are key:value pairs (associative array, map)

"""
[Python3: List vs Tuple vs Set vs Dictionary]
https://blog.softhints.com/python-list-vs-tuple-vs-dictionary-vs-set/

Lists:  for ordered collection of items or sequence of objects, var = [1, 2, '3']
[]      indexed, _not_ hashable

Tuples: can be considered as immutable list, var = (1, '2', 3.14) or var = 1, '2', 3.14
()      elements can't be added, removed or replaced after declaration,
        only index() and count() method,
        immutable, ordered, hashable, _not_ indexed

Sets:   unique list w/o order and duplicates, var = set()
set()   fast + union/intersection operations/methods,
        not hashable

Dict:   pair of key and values, var = {'key1':value,...}
{}      requires lookup by key or value,
        every key requires a value,
        values can be added, removed or modified values of dictionaries,
        indexed keys, no ordering
"""

# import some functions and classes [doesn't work if filenames start w/ numbers eg. 98_test]
# explicitly calling '__import__' builtin might help # strhx = __import__('98_test')
from modules import strhx, now, nowf, color
import time
import hashlib

tstart = time.time()
print('\nstart:', tstart, now(), nowf(), '\n')

print('>>> import strhx(), now(), nowf(), color() from file "modules"\n>>> from modules import strhx, now')
print('>>> now():', type(now))
print('>>> strhx():',type(strhx))
print('>>> strhx.__doc__: ',strhx.__doc__,sep='')

# associative array or map = dictionary (json like key:value pairs) in python

post_plain = {'user_id':209,'message':'hex representated message','language':'English','datetime':'20210804T134904Z','location':(44.590533, -104.715556)}
post_hex = {'user_id':209,'message':strhx(str(post_plain['message'])),'language':'English','datetime':'20210804T134904Z','location':(44.590533, -104.715556)}

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
print('''\n>>> indirectly access dict items using index[0] but requires to create an additional list
>>> index is only available using this list, not the plain dict !
post_plain_index = list(post_plain.keys())''', sep='\n')
print('\n', post_plain.keys(), '\nprint(post_plain_index[0]): ', post_plain_index[0], sep='')

# create hash objects for user_id value
print('''\n>>> create utf-8 encoded hash object 'post_plain_hash' for user_id
post_plain_hash = hashlib.sha256(str(post_plain['user_id']).encode('utf-8'))''')
post_plain_hash = hashlib.sha256(str(post_plain['user_id']).encode('utf-8'))
print('\npost_plain_hash: ', post_plain_hash, '\ntype: ', type(post_plain_hash))

# create digest / hex representation of hash object
print('''\n>>> create hex representation of hash object 'post_plain_hash'
post_plain_digest = post_plain_hash.hexdigest()''')
post_plain_digest = post_plain_hash.hexdigest()
print('\npost_plain_digest: ', post_plain_digest, '\ntype: ', type(post_plain_digest))

# add additional key:value pairs to dict
print('''\n>>> add new key 'hash' with sha256 value of 'user_id' (post_plain_digest) to dict post_plain''')
print('''post_plain['hash'] = post_plain_digest''')
post_plain['hash'] = post_plain_digest
print('\n',post_plain.keys(),sep='')

# update value for key in dict from dict2 post_plain_update w/ same key
print('''\n>>> update value in post_plain['location'] using post_plain.update() method and
>>> 2nd dictionary 'post_plain_update' as input''')
post_plain_update = {'location':(94.590533, -24.715556)}
print('''\ndict1:\npost_plain key ['location']:''', post_plain['location'])
print('''\ndict2:\npost_plain_update key ['location']:''', post_plain_update['location'])
print('\nupdate keys in both dictionaries\npost_plain.update(post_plain_update), post_hex.update(post_plain_update)')
post_plain.update(post_plain_update)
post_hex.update(post_plain_update)
print('''\n>>> post_plain, post_hex updated keys ['location']:\n
post_plain['location']: ''', post_plain['location'], '''
post_hex['location']: ''', post_hex['location'], '\n\nnow both match post_plain_update', sep='')

# hex conversion / compare
print('\n>>> use imported strhx function for message conversion to hex string')
print('''\npost_plain['message']:\n''', post_plain['message'], type(post_plain['message']),sep='\n')
print('''\npost_hex['message]:\n''', post_hex['message'], type(post_hex['message']),sep='\n')

# note, no hash in post_hex dict, update does not create keys
print('\nNOTE: no hash key in post_hex! we only added it to post_plain\n\npost_plain:', post_plain, '\npost_hex:', post_hex, sep='\n')

# arbitrary value for compare test
print('\n>>> compare hex values w/ db')
hx = '7b27757365725f6964273a203230392c20276d657373616765273a20273638363537383230373236353730373236353733363536653734363137343635363432303664363537333733363136373635272c20276c616e6775616765273a2027456e676c697368272c20276461746574696d65273a20273230323130383034543133343930345a272c20276c6f636174696f6e273a202839342e3539303533332c202d32342e373135353536297d'
hx_msg = '68657820726570726573656e7461746564206d657373616765'
hx_all = strhx(str(post_hex))

# print('\nhx_all (whole dictionary):',hx_all,sep='\n')
# print(type(hx_all))
print('\nhx_msg:',hx_msg)
print('\npost_hex[\'message\']:',post_hex['message'])

if post_hex['message'] == hx_msg:
    print('\n>>> VALUE MATCH')
else:
    print('\n>>> VALUE NO_MATCH')

print('\n>>> compare hex for complete dict')
if hx_all == hx:
    print('\ninput:',hx_all,'\nmsg:',hx,'\n>>> MATCH',sep='\n')
else:
    print('\ninput:',hx_all,'\nmsg:',hx,'\n>>> NO_MATCH',sep='\n')

time.sleep(1)
tend = time.time()
print(color.DARKYELLOW,'\nt_started  :', color.CYAN, tstart, color.END)
print(color.DARKYELLOW,'\nt_finished :', color.DARKCYAN, time.time(), color.END)
print(color.DARKYELLOW,'\nt_duration :', color.DARKGRAY, tend - tstart)
print('\n', color.BOLD,now(),color.UNDERLINE,color.DARKGRAY,' ', nowf(), color.END, '\n', sep='')
