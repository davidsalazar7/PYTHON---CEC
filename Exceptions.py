# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:18:25 2020

@author: CEC
"""
'''
try:
    print('1')
    x=1/0
    print('2')
except:
    print('Something went wrong')
print('3')
'''

'''
try:
    x=int(input('Enter a number: ' ))
    y=1/x
    print(y)
except ZeroDivisionError:
    print('Cannot divide by 0')
except ValueError:
    print('Enter an integer value')
except:
    print('Something went wrong')
print('THE END')
'''

'''
try:
    y=1/0
    print(y)
except ZeroDivisionError:
    print('Zero division')
except ArithmeticError:
    print('Arithmetic problem')
print('THE END')
'''

'''
def badFun(n):
    try:
        return 1/n
    except ArithmeticError:
        print('Arithmetic problem')
    return None
badFun(0)
print('THE END')
'''

'''
def validarNumero(prompt, min, max):
    while (True):
        try:
            x = int(input(prompt))
            assert x >= min and x <= max
            return x
            break
        except ValueError:
            print("Ingresar solo numeros")
        except:
            print("El valor debe estar dentro del RANGO --> (-10..10) <--")
    
v = validarNumero("Ingrese un valor desde -10 a 10:", -10, 10)

print("El número es:", v)
'''
class TheSimplestClass:
    pass

myFirstObject=TheSimplestClass()
mySecondObject=TheSimplestClass()
myThirdObject=TheSimplestClass()
myFourthObject=TheSimplestClass()




