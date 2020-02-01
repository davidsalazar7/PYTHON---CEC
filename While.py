while True:
    FN=input("Nombre? ")
    LN=input("Apellido? ")
    ADD=input("Dirección? ")
    AGE=input("Edad? ")
    SPC=(" ")
   
    AGE=int(AGE)
    
    if 1<=AGE<=10:
        x="niño"
    elif 11<=AGE<=20:
        x="joven"
    else:
        x="viejo"

    print("Hola"+SPC+FN+SPC+LN+SPC+"con dirección"+SPC+ADD+SPC+"y"+SPC+str(AGE)+SPC+"años"+SPC+"("+x+")")

    continuar=input("Continuar? ")
    if continuar=="n":
        break
        
'''
while True:
    FN=input("Nombre? ")
    if FN=='q':
        break
    LN=input("Apellido? ")
    if LN=='q':
        break
    ADD=input("Dirección? ")
    if ADD=='q':
        break
    AGE=input("Edad? ")
    if AGE=='q':
        break
    SPC=(" ")
    
    AGE=int(AGE)
    
    if 1<=AGE<=10:
        x="niño"
    elif 11<=AGE<=20:
        x="joven"
    else:
        x="viejo"
    
    print("Hola"+SPC+FN+SPC+LN+SPC+"con dirección"+SPC+ADD+SPC+"y"+SPC+str(AGE)+SPC+"años"+SPC+"("+x+")")
'''