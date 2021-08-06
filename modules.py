import datetime
import sys
from time import sleep
from subprocess import call

# reset terminal using subprocess.call()
def term_reset():
    _ = call('reset')

# strings to hex representation
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

# progress spinner using generator w/ some help from [https://stackoverflow.com/a/4995896]
# def spinit():
def spinit(n=9):
    # create generator, note keyword 'yield' instead of 'return'
    def spin():
        while True:
            for cursor in '|/-\\':
                yield cursor
    spinner = spin()
    # initial value = 2 spins
    for i in range(1,n):
        # print('>>>',end=' ',sep='')
        # print(str(i),'',end='',sep='\r')
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        sleep(0.5)
        sys.stdout.write('\b')

# custom color output
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    # 256color foreground [38;5;$idm]
    DARKGRAY = '\033[38;5;240m'
    DARKYELLOW = '\033[38;5;136m'
    # non color ansi codes
    CLS = '\033[2J'

# print(color.DARKYELLOW, '\nfinished:', color.BOLD, color.GREEN, now(), color.CYAN, nowf(), color.END, '\n')
