# import module first
import datetime

# add some ansi colors and formats, see 0_ansi.md for reference
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    # 256color forground [38;5;$idm]
    DARKYELLOW = '\033[38;5;136m'
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
print('>>> print(today)\n')
print(today)
print('''\n>>> print today(microsecond) as formatted 'bold' + 'cyan' ansi concatenated string''')
print('>>> print(color.BOLD + color.CYAN + str(today.microsecond) + color.END)')
print('>>> format: %Y-%m-%d %H:%M:%S.%f')
print('>>> extra long concatenated stuff ^^')
print('''>>> print(
>>> str(today.date()) + ' ' +
>>> str(today.hour) + ':' +
>>> str(today.minute) + ':' +
>>> str(today.second) + '.' +
>>> color.BOLD + color.CYAN +
>>> str(today.microsecond) +
>>> color.END + color.DARKYELLOW +
>>> ' \\o/ yay, we have "256 color" colors !' +
>>> color.END)\n''')
print(str(today.date()) + ' ' + str(today.hour) + ':' + str(today.minute) + ':' + str(today.second) + '.' + color.BOLD + color.CYAN + str(today.microsecond) + color.END + color.DARKYELLOW + ' \\o/ yay, we have "256color" colors !' + color.END)

# string to datetime obj
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

print('convert string to datetime object')
print('>>> using datetime.datetime.strptime() string parse time method')
print('>>> given datestr = ' + '"' + color.BOLD + color.CYAN + '31.07.1977' + color.END + ', ' + color.YELLOW + '16:31:12' + color.END + '"')
print('>>> but should be parsed as python default datetime format')
print('>>> parsed datestr = ' + color.GREEN + "1977-07-31 16:31:12" + color.END + '\n')
print('given datestr = ' + color.BOLD + "31.07.1977, 16:31:12" + color.END)
datestr = "31.07.1977, 16:31:12"
print('\n>>> datecon = datetime.datetime.strptime(datestr, "%d.%m.%Y, %H:%M:%S")')
print('>>> type of \'datecon\':', type(datetime.datetime.strptime(datestr, "%d.%m.%Y, %H:%M:%S")))
datecon = datetime.datetime.strptime(datestr, "%d.%m.%Y, %H:%M:%S")
print('\nparsed datestring =', color.BOLD + str(datecon) + color.END + '\n\n' + color.PURPLE + 'works ;)\n' + color.END)
