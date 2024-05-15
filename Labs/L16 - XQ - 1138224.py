print("Semana 16: Ejercicio 1")
import random
lista=[]
for x in range (10):
    lista.append(random.randint(0,10))
print("Menú:", "1. mostrar numeros", "2. promedio","3. longitud del arreglo", "4. suma de posiciones" sep="\n")    
o=int(input("Ingrese una opcion: "))
match o:
    case 1:
        for i in range (0,10):
            print(lista[i])
    case 2:
        s=0
        for x in range (len(lista)):
            s += lista[x]
            p=s/len(lista)
            print("el promedio es", p)
    case 3:
        print("la longitud del arreglo es", len(lista))
    case 4: 
        pares=0
        impares=0
        for _ in range (0,10,2):
            pares+=lista[x]
        for a  in range (1,10,2):
            impares+=lista[a]
        print(f"La suma de pares es {pares} y la de impares es {impares}")

print("Semana 16: Ejercicio 2")
f=int(input("Ingrese la cantidad de filas: "))
c=int(input("Ingrese la cantidad de columnas: "))
matriz=[[0 for x in range (c)] for y in range(f)]
mayor=0
menor=1000
pares=[]
impares=[]
for xf in range(f):
    for xc in range(c):
        matriz[xf][xc]=random.randint(0,1000)
        if(matriz[xf][xc]>mayor):
            mayor=matriz[xf][xc]
        if(matriz[xf][xc]<menor):
            menor=matriz[xf][xc]
        if(matriz[xf][xc]%2==0):
            pares.append(matriz[xf][xc])
        elif (matriz[xf][xc]%2==0):
            impares.append(matriz[xf][xc])
print(f"el n° mayor es {mayor}, el menor es {menor}. Hay {len(pares)} n° pares y {len(impares)} n° impares")