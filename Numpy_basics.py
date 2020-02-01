import numpy as np
import time

SIZE=1000000

L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start=time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)

start=time.time()
result=A1+A2
print((time.time()-start)*1000)

#crear una matriz de unos - 3 filas 4 columnas
unos=np.ones((3,4))
print(unos)

#crear matriz de ceros - 3 filas 4 columnas
ceros=np.zeros((3,4))
print(ceros)

#crear una matriz con valores aleatorios
aleatorios=np.random.random((3,3))
print(aleatorios)

#crear una matriz vacía
vacia=np.empty((3,2))
print(vacia)

#crear una matriz con un solo valor
full=np.full((12,2),4)
print(full)

#crear una matriz con valores espaciados uniformemente
espacio1=np.arange(0,30,1)
print(espacio1)

#matriz con tantos valores entre un rango
espacio2=np.linspace(0,2,2)
print(espacio2)

#matriz identidad
identidad1=np.eye(4,4)
print(identidad1)

identidad2=np.identity(4)
print(identidad2)

#conocer las dimensiones de una matriz
a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)

#conocer el tipo de los datos
a=np.array([(1,2,3)])
print(a.dtype)

#conocer el tamaño y forma de la matriz
a=np.array([(1,2,3,4,5,6)])
print(a.size)
print(a.shape)

#cambio de forma de una matriz
a=np.array([(8,9,10),(11,12,13)])
print(a)
print("\n"*2)
a=a.reshape(3,2)
print(a)

a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print(a[1,2])
print(a[0:,1]) #valor de todas las filas

#min, max y suma
a=np.array([(2,4,8)])
print(a.min())
print(a.max())
print(a.sum())

#raiz cuadrada y desviacion estandar
a=np.array([(1,2,3),(3,4,5)])
print("\n"*2)
print(np.sqrt(a))
print("\n"*2)
print(np.std(a))

#operaciones con matrices
x=np.array([(1,2,3),(3,4,5)])
y=np.array([(1,2,3),(3,4,5)])

print(x+y)
print(x-y)
print(x*y)
print(x/y)










