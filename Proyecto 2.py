Columnas=[]
NColumnas=[]
def validaciones(p,c,e,f):
        if e=='a':
            col=0
        elif e=='b':
            col=1
        elif e=='c':
            col=2
        elif e=='d':
            col=3
        elif e=='e':
            col=4
        elif e=='f':
            col=5
        elif e=='g':
            col=6
        elif e=='h':
            col=7
        else:
            print("Ingrese una columna valida")
        if 1>f>8:
            print("ingrese una fila valida")
        if Tabla[f-1][col]=='.':
            for _ in range(8):
                for k in range(8):
                    Tabla[f-1][col]=p,c
            Columnas.append(e)
            NColumnas.append(col)
        else:
            print("La posicion ya está tomada, vuelva a comenzar") 
#Llenar el tablero
n=int(input("Ingrese la cantidad de piezas en el tablero: "))
Tabla = [['.' for _ in range(8)] for _ in range(8)]
print("Rey", "Reina", "Arfil", "Caballo", "Peón", sep="\n")
for i in range(0,n):
    p=input("Ingrese el tipo de pieza que desea: ")
    c=input("¿La pieza será blanco o negro? ")
    e=input("Ingrese la columna de ubicación (a-h): ")
    f=int(input("Ingrese la fila de ubicación (1-8): "))
    validaciones(p,c,e,f)
#datos de la torre
ct=input("¿La torre será blanco o negro? ") 
et=input("Ingrese la columna de ubicación (a-h): ")
ft=int(input("Ingrese la fila de ubicación (1-8): "))
validaciones('Torre', ct,et,ft)
#Impresión
for f in Tabla:
    print(f)
#movimientos derecha
if (NColumnas[n]+1)>=8:
    print("Sin movimientos a la derecha")
else:
    for i in range((NColumnas[n]+1),8,1):
        if Tabla[ft-1][i]=='.':
            if i==0:
                ii='a'
            elif i==1:
                ii='b'
            elif i==2:
                ii='c'
            elif i==3:
                ii='d'
            elif i==4:
                ii='e'
            elif i==5:
                ii='f'
            elif i==6:
                ii='g'
            elif i==7:
                ii='h'
            print(f"Puede ir a: {ii}{ft}")
        else:
            print(f"derecha: El paso está obstruido por {Tabla[ft-1][i]}")
            break
#movimientos izquierda
if (NColumnas[n]-1)<=-1:
    print("Sin movimientos a la izquierda")
else:
    for i in range((NColumnas[n]-1),-1,-1):
        if Tabla[ft-1][i]=='.':
            if i==0:
                ii='a'
            elif i==1:
                ii='b'
            elif i==2:
                ii='c'
            elif i==3:
                ii='d'
            elif i==4:
                ii='e'
            elif i==5:
                ii='f'
            elif i==6:
                ii='g'
            elif i==7:
                ii='h'
            print(f"Puede ir a: {ii}{ft}")
        else:
            print(f"izq: El paso está obstruido por {Tabla[ft-1][i]}")
            break
#movimientos arriba
if ft-2<=-1:
        print("Sin movimientos hacia arriba")
else:
    for i in range(ft-2,-1,-1):
        if Tabla[i][NColumnas[n]]=='.':
            print(f"Puede ir a: {Columnas[n]}{i+1}")
        else:
            print(f"arriba: El paso está obstruido por {Tabla[i][NColumnas[n]]}")
            break
#movimientos abajo
if ft+1>=8:
        print("Sin movimientos hacia abajo")
else:
    for i in range(ft,8):
        if Tabla[i][NColumnas[n]]=='.':
            print(f"Puede ir a: {Columnas[n]}{i+1}")
        else:
            print(f"abajo: El paso está obstruido por {Tabla[i][NColumnas[n]]}")
            break