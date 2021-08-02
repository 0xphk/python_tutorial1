# import module first
import datetime

# add some ansi colors and formats
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

print('\n# print available classes in module datetime')
print(dir(datetime))

print('\n# get help for classes')
print('>>> help(datetime.time)')

# set some attributes to test object 'gvr'
print('\n# birthday of guido van rossum as {gvr} variable')
print('>>> gvr = datetime.date(1956, 1, 31)')
gvr = datetime.date(1956, 1, 31)

print('print whole object {gvr} date:', gvr)
print('print only {gvr.year}:', gvr.year)
print('print only {gvr.month}:', gvr.month)
print('print only {gvr.day}:', gvr.day)

print('\nusing {dateime.timedelta}')
print('>>> mill = datetime.date(2000, 1, 1)')
mill = datetime.date(2000, 1, 1)

# timedelta pos number increase, neg number decrease
print('>>> dtplus = datetime.timedelta(100)')
dtplus = datetime.timedelta(100)
print('>>> dtminus = datetime.timedelta(-100)')
dtminus = datetime.timedelta(-100)

print('\ncalculate date from timedelta {mill} + {dtplus}:')
print('>>> print(mill + dtplus)')
print('100 days after mill, date:', mill + dtplus)

print('\ndefault date format 1970-1-1')
print('>>> default format for datetime is: yyyy-mm-dd')

print('\nset own date format: "Day-name, Day_#month-name, Day-#, Year"')
print('>>> old method: print(gvr.strftime("%A, %B, %d, %Y")')
print(gvr.strftime("%A, %B %d, %Y"))
print(gvr.strftime("%A, %dst %B, %Y"))

print('\ndefine format using variable:')
print('>>> message = "GVR was born {:%A, %B %d, %Y}."')
message = "GVR was born {:%A, %B %d, %Y}."
print('>>> print(message.format(gvr))')
print(message.format(gvr))

print('\ncombine date and time')
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
# does not work
#launch_datetime = datetime.datetime(int(launch_date), int(launch_time))

print('''>>> launch_date = datetime.date(2017, 3, 30)
>>> launch_time = datetime.time(22, 27, 0)
>>> launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)''')
print('\nprint individual attributes from launch_date:\nday:', launch_date.day, 'month:', launch_date.month, 'year:', launch_date.year)
print('launch_date:', launch_date)
print('\nprint individual attributes from launch_time:\nhour:', launch_time.hour, 'minute:', launch_time.minute, 'seconds:', launch_time.second, 'and even microseconds:', launch_time.microsecond)
print('launch_time:', launch_time)
print('\nprint individual attributes from launch_datetime:\nday:', launch_date.day, 'month:', launch_date.month, 'year:', launch_date.year, '\nhour:', launch_time.hour, 'minute:', launch_time.minute, 'seconds:', launch_time.second, 'and even microseconds:', launch_time.microsecond)
print('launch_datetime:', launch_datetime)

# access current date datetime.datetime.today()
print('\naccess current datetime using method datetime.datetime.today()')
print('>>> today = datetime.datetime.today()')
today = datetime.datetime.today()
print('>>> method displays microseconds as well')
print('>>> print(today)')
print(today)
print('''>>> print today(microsecond) as formatted 'bold' + 'cyan' ansi concatenated string''')
print('>>> print(color.BOLD + color.CYAN + str(today.microsecond) + color.END)')
print(color.BOLD + color.CYAN + str(today.microsecond) + color.END + ' yay, we have colors !\n')
