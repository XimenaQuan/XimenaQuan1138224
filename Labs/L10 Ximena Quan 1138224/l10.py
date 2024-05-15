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

#Actividad 2
print("Semana 10: ejercicio 2")
a=int(input("ingrese un número a mayor a 0")) #entradas
b=int(input("ingrese un número b mayor a 0"))
c=int(input("ingrese un número c mayor a 0"))
if a<=0 or b<=0 or c<=0: #validación
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
else: 
    if b>c:
        print(b)
    elif b==c:
        print(b,c)
    else: 
        print(c)

#Actividad 3
print("semana 10: ejercicio 3 \n")
print("Ximena Quan - 1138224 \n")
d1=int(input("ingresa tu dia de nacimiento \n"))
m1=int(input("ingresa tu mes de nacimiento en número \n"))
f=int(input("ingresa tu año de nacimiento \n"))
s1=""
if (m1==1 and 1<=d1<20) or (m1==12 and 19<d1<31):
    print("Capricornio")
elif (m1==2 and 1<=d1<18) or (m1==1 and 20<=d1<31):
    print("Acuario")
elif (m1==3 and 1<=d1<20) or (m1==2 and 18<=d1<28):
    print("Piscis")
elif (m1==4 and 1<=d1<20) or (m1==3 and 20<=d1<31):
    print("Aries")
elif (m1==5 and 1<=d1<20) or (m1==4 and 20<=d1<30):
    print("Tauro")
elif (m1==6 and 1<=d1<20) or (m1==5 and 20<=d1<31):
    print("Geminis")
elif (m1==7 and 1<=d1<20) or (m1==6 and 20<=d1<30):
    print("Cancer")
elif (m1==8 and 1<=d1<20) or (m1==7 and 20<=d1<31):
    print("Leo")
elif (m1==9 and 1<=d1<20) or (m1==8 and 20<=d1<30):
    print("Virgo")
elif (m1==10 and 1<=d1<20) or (m1==9 and 20<=d1<31):
    print("Libra")
elif (m1==11 and 1<=d1<20) or (m1==10 and 20<=d1<30):
    print("Escorpio")
elif (m1==12 and 1<=d1<20) or (m1==11 and 20<=d1<31):
    print("Sagitario")
