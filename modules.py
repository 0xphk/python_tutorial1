import datetime

def strhex(i):
    """returns hex value for given string"""
    # prints 2 times?
    # print(i)
    ie = i.encode("utf-8").hex()
    return ie
# print(strhex.__doc__)
# print(strhex('phk'))

now = datetime.datetime.today()
# print('script finished', now, '\n')
