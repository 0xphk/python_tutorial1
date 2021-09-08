# basic math
from modules import Calc
import calc
import inspect

print(9 + 2)

print(-9 + 2)

print(8 * 3)

print(8 / 2)

# . before -
print(8 + 2 / 4 + 1)

print((8 + 2) / (4 + 1))

# combine string + calc
result = eval('9 + 2')
print("result is:", result)
print("result is:", (9 + 2))
print()

# simple calc module
print('>>> import calc module:',end=' ')
print(inspect.getsource(calc))

print('10 + 5 = ',calc.add(10,5))
print('10 / 5 = ',int(calc.div(10,5)))
print('10 * 5 = ',calc.mul(10,5))
print('div as float:',calc.add(calc.mul(10,5),calc.div(100,10)))
print('div as int:',calc.add(calc.idiv(10,5),calc.mul(100,10)))
print('result float as type int:',int(calc.add(calc.div(10,5),calc.mul(100,10))))
print()

print('>>> import class Calc:',end=' ')
print(inspect.getsource(Calc))

print('10 + 5 = ',Calc.add(10,5))
print('10 / 5 = ',int(Calc.div(10,5)))
print('10 * 5 = ',Calc.mul(10,5))
print('div as float:',Calc.add(Calc.mul(10,5),Calc.div(100,10)))
print('div as int:',Calc.add(Calc.idiv(10,5),Calc.mul(100,10)))
print('result float as type int:',int(Calc.add(Calc.div(10,5),Calc.mul(100,10))))
print()
print('remainder of 10 / 3 = ',Calc.rdiv(10,3))
print('8 to the power of 2 (8^2) = ',Calc.exp(8,2))

# print primes between lower - upper
lower = 900
upper = 1000

for num in range(lower, upper + 1):
    # all primes are > 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
