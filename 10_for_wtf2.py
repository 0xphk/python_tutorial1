#################################
# REALLY STRANGE BUG / WHATEVER #
#################################
# i dont get it, in plain shell it works as expected, wtf is wrong here
# up = int(input('up: '))
# TypeError: 'int' object is not callable'''

# count backwards - works with var = int but not from str input typecasted to int??
upper = 10
for i in range(upper,-1,-1):
    print(i)

# moving this code to seperate file it starts working wtf
up = int(input('up: '))
for r in range(up, -1, -1):
    print(r)
