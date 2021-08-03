import datetime

def strhx(i):
    """returns hex value for given string\nremember to use str() as input"""
    # prints 2 times?
    # print(i)
    ie = i.encode("utf-8").hex()
    return ie
# print(strhx.__doc__)
# print(strhx('phk'))

now = datetime.datetime.today()
# print('script finished', now, '\n')
