from modules import strhx
import random

rotate = bytes.maketrans(
    b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    b"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")

# prepare empty list
rlist = []

# fill list w/ random elements
count = 0
while count < 99:
    count += 1
    rint = random.randint(1000, 9999)
    rhex1 = random.randbytes(4).hex()
    rhex2 = random.randbytes(4).hex()
    rstr = str(rhex1 + str(rint) + rhex2)
    rlist.append(rstr)

# add not so random index 0
rhead = 'not!_so_random_stuff'
rthead = strhx(rhead.translate(rotate))
rlist.insert(0,rthead)

# intermediate list to keep track of usedItems
rlistUsed = []
rlistUsed.extend(rlist)
usedItems = set()
usedIndex = set()

print('''\n>>> Select 10 random elements from dynamic list "rlist"
>>> do not allow index 0 or any duplicates\n''')

# debug: verify value, str.len(), rand_list.__len__()
# print('>>> list:',rlist,sep='\n')
# print('>>> rhead:',rhead,len(rhead),type(rhead))
# print('>>> rthead:',rthead,len(rthead),type(rthead))
# print('>>> rstr.len():',len(rstr),'\n>>> rlist.__len__():',rlist.__len__())

count = 0
while count < 10:
    # get 10 random items from list, remove used items from list
    count += 1
    rlistIndex = random.randint(1,99)
    rlistItem = rlist[rlistIndex]

    # prevent selecting already used index
    while rlistIndex in usedIndex:
        # repeat choice
        rlistIndex = random.randint(1,99)
        rlistItem = rlist[rlistIndex]

    usedItems.add(rlistItem)
    usedIndex.add(rlistIndex)

    # remove element by index
    # del rlistUsed[rlistItem]

    # remove element by match
    rlistUsed.remove(rlistItem)

    print(f'index: {rlistIndex:02d} {rlistItem}')
    
    # randchoice - better use randint as choice can not blacklist index
    # rlistItem = random.choice(rlist)  # includes index 0
    # rlistIndex = rlist.index(rlistItem)
    # print(f'index: {rlistIndex:02d} {rlistItem}')
    # rlistUsed.remove(rlistItem)
    
    # randint
    # rlistItem = random.randint(1,99)
    # add leading zero to single-figure number index using fstring{int:02d}
    # print(f'index: {rlistItem:02d} {rlist[rlistItem]}')
    # print(f'index: rlistItem {rlistItem} {rlist[rlistItem]}')

# print(usedItems)
print(f'\n>>> used indices:\n{usedIndex}')

# print(rlistUsed)

print('\n>>> used items removed from intermediate list: rlistUsed\n>>> rlistUsed.__len__():',rlistUsed.__len__())
print('\n>>> original list untouched: rlist\n>>> rlist.__len__():',rlist.__len__())
