from modules import strhx
import random

rlist = []
rotate = bytes.maketrans(
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
rhead = 'not!_so_random_stuff'
rthead = strhx(rhead.translate(rotate))
rlist.insert(0,rthead)

# verify value, str.len(), rand_list.__len__()
print('>>> list:',rlist,sep='\n')
print('>>> rhead:',rhead,len(rhead),type(rhead))
print('>>> rthead:',rthead,len(rthead),type(rthead))
print('>>> rstr.len():',len(rstr),'\n>>> rand_list.__len__():',rlist.__len__())
print('>>> 10 random items from rlist\n')

count = 0
while count < 10:
    # get 10 random items from list, dupes possible, fix this!
    count += 1
    rlistItem = random.randint(1,99)
    # add leading zero to single-figure number index using fstring{int:02d}
    print(f'index: {rlistItem:02d} {rlist[rlistItem]}')
