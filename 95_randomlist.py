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

# not so random index 0
rhead = 'not!_so_random_stuff'
rthead = strhx(rhead.translate(rotate))
rlist.insert(0,rthead)

# intermediate list to keep track of usedItems
rlistUsed = []
rlistUsed.extend(rlist)

# verify value, str.len(), rand_list.__len__()
print('>>> list:',rlist,sep='\n')
print('>>> rhead:',rhead,len(rhead),type(rhead))
print('>>> rthead:',rthead,len(rthead),type(rthead))
print('>>> rstr.len():',len(rstr),'\n>>> rand_list.__len__():',rlist.__len__())
print('\n>>> 10 random items from rlist')

count = 0
while count < 10:
    # get 10 random items from list, remove used items from list
    count += 1
    rlistItem = random.choice(rlist)
    usedItems = set()
    usedItems.add(rlistItem)
    rlistIndex = rlist.index(rlistItem)
    print(f'index: {rlistIndex:02d} {rlistItem}')
    rlistUsed.remove(rlistItem)
    
    # randint instead of randchoice works too
    # rlistItem = random.randint(1,99)
    # add leading zero to single-figure number index using fstring{int:02d}
    # print(f'index: {rlistItem:02d} {rlist[rlistItem]}')
    # print(f'index: rlistItem {rlistItem} {rlist[rlistItem]}')

print('\n>>> used items removed from intermediate list: rlistUsed\n>>> rlistUsed.__len__():',rlistUsed.__len__())
print('\n>>> original list untouched: rlist\n>>> rlist.__len__():',rlist.__len__())
