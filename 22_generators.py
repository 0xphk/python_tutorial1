# converts function in generator using 'yield' keyword
from modules import term_reset, spinit

# function to match character 'e' in string
def printresult(String):
    for i in String:
        if i == "e":
            yield i

# initializing string
String = "GeeksforGeeks"

# var init value, used for calculate count of "e" in 'String'
ans = 0

# reset term
term_reset()

# fprint status line, no newline
print(f"The number of 'e' in word {String} == ",end="")

# spin cursor
spinit(6)

# strip does nothing here
# String = String.strip()

# increment 'ans' w/ 'yield' return values
for j in printresult(String):
    ans = ans + 1

print(ans)
