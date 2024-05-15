print("Semana 12: Ejercicio 1")
print("a sumatoria", "b factorial", "c tablas de multiplicar", "d número perfecto", sep="\n")
op=input("ingrese la elección: ")
match op:
    case "a":
        a=int(input("ingrese el n° limite de la sumatoria: "))
        if a<=0:
            print("error, debe ser positivo")
        else: 
            s=0
            i=1
            while(i<=a):
                s=s+i
                i=i+1
            print("la sumatoria es: ", s)
    case "b":
        b=int(input("ingrese el n° del factorial"))
        if b<0:
            print("error, debe ser positivo")
        else: 
            s=1
            i=1
            while(i<=b):
                s=s*i
                i=i+1
            print("el factorial es: ", s)
    case "c":
        col="\t"
        for x in range(1,11):
            col=col+str(x)+"\t"
        print(col, "\n")
        for f in range(1,11):
            f2=str(f)+"\t"
            for col2 in range(1,11):
                f2=f2+str(f*col2)+"\t"
            print(f2, "\t")
    case "d":
        d = int(input("Ingrese un número entero mayor a cero: "))
        f = 0
        for i in range(1, d):
            if (d % i == 0):
                f = i + f
        if (f == d):
            print (d, "Es perfecto")
        else:
            print (d, "No es perfecto")
    case _:
        print ("Elija una opción válida")