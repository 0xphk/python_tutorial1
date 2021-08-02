# import module first
import datetime

print('\n# print available classes in module datetime')
print(dir(datetime))

print('\n# get help for classes')
print('>>> help(datetime.time)')

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

print('\ncalculate date from timedelta {mill} + {dtplus}\n')
print('100 days after mill, date:', mill + dtplus)

