print("Semana 12: Ejercicio 1")
print("1) Area de un triangulo","2) Area de un cuadrado","3) Area de un rectangulo","4) Area de un circulo",sep="\n")
def triangulo():
    b=int(input("Ingrese la base: "))
    h=int(input("Ingrese la altura: "))
    print("El area es: ", (b*h)/2)
def cuadrado():
    l=int(input("Ingrese el lado: "))
    print("El area es: ", l**2)
def rectangulo():
    b=int(input("Ingrese la base: "))
    h=int(input("Ingrese la altura: "))
    print("El area es: ", b*h)
def circulo():
    b=int(input("Ingrese el radio: "))
    print("El area es: ", 3.1416*(b**2))
a=True
while a==True:
    n=int(input("Ingrese una opción: "))
    match n:
        case 1:
            triangulo()
            a=True
        case 2:
            cuadrado()
            a=True
        case 3: 
            rectangulo()
            a=True
        case 4:
            circulo()
            a=True