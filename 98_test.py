def strhex(i):
    """returns hex value for given string"""
    # prints 2 times?
    print('>>>', i)
    return i.encode("utf-8").hex()
print(strhex.__doc__)
print(strhex('phk'))
