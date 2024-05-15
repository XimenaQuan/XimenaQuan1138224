print("Semana 11: Ejercicio 1")
n=int(input("ingrese un número mayor a 0 "))
a=0
b=1
c=0
i=2
r=""
if n>0: 
    r=str(a)
    if(n>1):
        r+= "," + str(b)
    while(i<n):
        c=a+b
        r += "," + str(c)
        a=b
        b=c
        i=i+1 
    print(r)
else:
    print(r)

print("Semana 11: Ejercicio 2")
p=int(input("ingrese un entero mayor a 0 "))
if p<=0:
    print("Error, debe ser mayor a 0")
r2=0
r3=0
r4=0
for m in range (1,p+1):
    r2+=(1/m)
    r3+=(1/2**m)
print("insciso a) ", r2)
print("insciso b) ", r3)    
x=int(input("ingrese un entero mayor a 0 x "))
y=int(input("ingrese un entero mayor a 0 y "))
for k in range (0, p+1):
    r4+=(x**k)*(y**(p-k))
print("insciso c) ", r4)
