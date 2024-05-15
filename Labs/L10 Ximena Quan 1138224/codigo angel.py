print("semana 10: ejercicio 1")
m=int(input("ingrese un número del 1-12 \n"))
s=""
match m:
    case 1:
        s= "enero"
    case 2:
        s= "febrero"
    case 3:
        s= "marzo"
    case 4:
        s= "abril"
    case 5:
        s= "mayo"
    case 6:
        s= "junio"
    case 7:
        s= "julio"
    case 8:
        s= "agosto"
    case 9:
        s= "septiembre"
    case 10:
        s= "octubre"
    case 11:
        s= "noviembre"
    case 12:
        s= "diciembre"
    case _:
        print("Error, el número debe estar entre 1 y 12")
print(f"Mes:{s}")


print("Semana 10: ejercicio 2")
a=int(input("ingrese un número a mayor a 0")) 
b=int(input("ingrese un número b mayor a 0"))
c=int(input("ingrese un número c mayor a 0"))
if a<=0 or b<=0 or c<=0: 
    print("Error, el número debe ser mayor a 0")
if a>b:
    if a>c:
        print(a)
    else: 
        if a==c: 
            print(a,c)
        else: 
            print(a,b)
elif a==b:
    if a>c:
        print(a,b)
    elif a==c:
        print("los 3 son iguales") 
    else: 
        print(c)

print("Semana 10: ejercicio 3")

ndia = int(input("Coloque su dia de nacimiento: "))
nmes =int (input("Coloque su mes de nacimiento"))
naño= int (input("Coloque el año de nacimiento"))
if (nmes == 3 and ndia>=21) or (nmes==4 and ndia<=19): 
        print("Su signo zodiacal es Aries")
elif (nmes == 4 and ndia>=20) or (nmes==5 and ndia<=20):
    print("Su signo zodiacal es Tauro")
elif (nmes == 5 and ndia>=21) or (nmes==6 and ndia<=20):
    print("Su signo zodiacal es Geminis")
elif (nmes == 6 and ndia>=21) or (nmes==7 and ndia<=22):
    print("Su signo zodiacal es Cancer")
elif (nmes == 7 and ndia>=23) or (nmes==8 and ndia<=22):
    print("Su signo zodiacal es Leo")
elif (nmes == 8 and ndia>=23) or (nmes==9 and ndia<=22):
    print("Su signo zodiacal es Virgo")
elif (nmes == 9 and ndia>=23) or (nmes==10 and ndia<=22):
    print("Su signo zodiacal es Libra")
elif (nmes == 10 and ndia>=23) or (nmes==11 and ndia<=21):
    print("Su signo zodiacal es Escorpio")
elif (nmes == 11 and ndia>=22) or (nmes==12 and ndia<=21):
    print("Su signo zodiacal es Sagitario")
elif (nmes == 12 and ndia>=22) or (nmes==1 and ndia<=19):
    print("Su signo zodiacal es Capricornio")
elif (nmes == 1 and ndia>=20) or (nmes==2 and ndia<=18):
    print("Su signo zodiacal es Acuario")
elif (nmes == 2 and ndia>=19) or (nmes==3 and ndia<=20):
    print("Su signo zodiacal es Pisis")
