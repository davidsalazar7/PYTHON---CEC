str1="Cisco"
str2="Networking"
str3="Academy"
space=" "
print(str1+space+str2+space+str3)
print(str1+str2+str3)
#separar strings
print(str1,str2,str3)

x=3
print("This value of X is " , x)
print("This value of X is " + str(x))
print(type(x))
x=str(x)
print(type(x))

pi=22/7
print(pi)
print("{:.4f}".format(pi))

#listas
hostnames=["R1","R2","R3","S1","S2"]
print(hostnames)
print(type(hostnames))
len(hostnames)
print(hostnames[-2])
#reasignar valor a index 0
hostnames[0]="R1_C"
print(hostnames[0])
#eliminar index 2
del hostnames [2]
print(hostnames)

list_ex=["R1",3,True,"S1",3.14]
print(list_ex)
print(type(list_ex))
len(list_ex)
print(list_ex[1])

#Input
firstName=input("Fist Name? ")
print("Hello "+firstName+"!")
