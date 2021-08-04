import datetime

def strhx(i):
    """returns hex value for given input - expects str()"""
    # prints 2 times?
    # print(i)
    ie = i.encode("utf-8").hex()
    return ie
# print(strhx.__doc__)
# print(strhx('phk'))

def dtformat():
    """format options for datetime objects"""
    print('''\ncustom datetime formatting:

    >>> time
    >>> %Z - timezone name
    >>> %z - UTC offset +HHMM or -HHMM
    >>> %p - locales equivalent am or pm
    >>> %I - 12h hour as zero padded decimal number
    >>> %H - 24h hour as zero padded decimal number
    >>> %M - minute as zero padded decimal number
    >>> %S - second as zero padded decimal number
    >>> %f - microsecond as zero padded decimal number

    >>> day, weekday
    >>> %d - day of month as zero padded decimal number
    >>> %j - day of the year as as zero padded decimal number
    >>> %w - weekday as decimal number 0=Sunday 6=Saturday
    >>> %a - weekday abbreviated name
    >>> %A - weekday full name

    >>> year
    >>> %Y - year w/ century as decimal number
    >>> %y - year w/o century as zero padded decimal number

    >>> month
    >>> %B - months full name
    >>> %b - months abbreviated name
    >>> %m - month as zero padded decimal number\n''')
# print(dtformat())

# now = datetime.datetime.today()
def now():
    return datetime.datetime.today()

# nowf = datetime.datetime.strftime(format, now)
def nowf():
    format = "%Y%m%dT%H%M%SZ"
    return now().strftime(format)

print('\nfinished:', now(), nowf(), '\n')
