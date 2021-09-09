import time
import sys

# abs indent example
indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        # is never called but why?
        if indentIncreasing:
            indent = indent + 1
            print('wave: ' + str(indent))
            if indent == 20:
                # change direction
                indentIncreasing = False
        else:
            indent -= 1
            print('wave: ' + str(indent))
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
