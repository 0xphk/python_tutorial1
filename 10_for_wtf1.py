#################################
# REALLY STRANGE BUG / WHATEVER #
#################################
# i dont get it, in plain shell it works as expected, wtf is wrong here
# up = int(input('up: '))
# TypeError: 'int' object is not callable'''

# moving this code from 10_for_loops.py to seperate file it starts working wtf
up = int(input('up: '))
for r in range(up, -1, -1):
    print(r)
