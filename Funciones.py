'''
def message():
    print("Enter next value")
    
print("We start here")
message()
print("The end is here")

def hi(name):
    print("Hi,",name)
hi("Greg")

def hiAll(name1,name2):
    print("Hi,",name1)
    print("Hi,",name2)
hiAll("David","Konrad")

def address(street,city,postalcode):
    print("Your adrress is:",street,"St.",city,postalcode)
    
s=input("Street: ")
c=input("City: ")
pc=input("Postal Code: ")

address(s,c,pc)

def subtra(a,b):
    print(a-b)
    
subtra(10,2)
subtra(2,10)

def subtra(a,b):
    print(a-b)
    
subtra(a=10,b=2)
subtra(a=2,b=10)

def subtra(a,b):
    print(a-b)
    
subtra(5,b=2)
subtra(a=5,2) falla debido posicion

def multiply (a,b):
    return a*b

print(multiply(3,4))


def wishes():
    print("My Wishes")
    return "Happy Birthday"
wishes()


def wishes():
    print("My Wishes")
    return "Happy Birthday"
print(wishes())


def hiEverybody(myList):
    for name in myList:
        print ("Hi",name)
        
hiEverybody(["name1","name2","name3",2])


def createList(n):
    myList=[]
    for i in range(n):
        myList.append(i)
    return myList

print(createList(5))
    '''



