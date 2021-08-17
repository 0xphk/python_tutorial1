from modules import strhx
import random

rlist = []
rot13 = bytes.maketrans(
    b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    b"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")

count = 0
while count < 99:
    count += 1
    rint = random.randint(1000, 9999)
    rhex1 = random.randbytes(4).hex()
    rhex2 = random.randbytes(4).hex()
    rstr = str(rhex1 + str(rint) + rhex2)
    rlist.append(rstr)
rhead = 'totally_random_stuff'
rthead = strhx(rhead.translate(rot13))
rlist.insert(0,rthead)

print('rhead:',rhead,len(rhead),type(rhead))
print('rthead:',rthead,len(rthead),type(rthead))

# verify str.len(), rand_list.__len__()
print('rstr.len():',len(rstr),'\nrand_list.__len__():',rlist.__len__())

# print('list:',rlist,sep='\n')

count = 0
while count < 10:
    # get 10 random items from list
    count += 1
    rlistItem = random.randint(1,99)
    print('index:',rlistItem,rlist[rlistItem])
