def isPrime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

for i in range(0, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")

'''
while True:
    num = input('Ingrese un numero: ')
    if num == "q":
        break
    num = int(num)

    if isPrime(num) is True:
        print('Primo')
    else:
        print('No Primo')
'''
'''
print(isPrime(1))
'''
for i in range(4):
    print(i,end=(" "))

result=0
n=5
for i in range(1,n+1):
    result += i
print(result)

for i in range(10,0,-2):
    print(i,end=(" "))