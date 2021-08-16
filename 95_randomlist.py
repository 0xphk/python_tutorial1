import random
import base64

rlist = []

print()

count = 0
while count < 100:
    count += 1
    rint = random.randint(1000, 9999)
    rhex1 = random.randbytes(4).hex()
    rhex2 = random.randbytes(4).hex()
    rstr = str(rhex1 + str(rint) + rhex2)
    rlist.append(rstr)
rbhead = base64.b64encode(b'total_random_stuff')
# replace().replace() works but is ugly
rhead = str(rbhead).replace("b","",1).replace("'","")
print(rhead)
print('rhead:',rhead,type(rhead))

rlist.insert(0,rhead)

# do not understand this yet
# removeSpecialChars = z.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
# removeSpecialChars = rhead.translate ({ord(c): " " for c in "'b"})

# verify str.len(), rand_list.__len__()
print('rstr.len():',len(rstr),'\nrand_list.__len__():',rlist.__len__())
print('list:',rlist,sep='\n')

# print(rpl('12764513764'))
