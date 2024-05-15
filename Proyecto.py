import turtle 
turtle.screensize(300,300)
def margen():
    turtle.clearscreen()
    margen=turtle.Turtle()
    margen.hideturtle()
    margen.speed(300)
    margen.penup()
    margen.teleport(-300, 210)
    margen.pendown()
    margen.pencolor("black")
    for i in range (0,2):
        margen.forward(600)
        margen.left(90)
        margen.forward(40)
        margen.left(90)
    margen.penup()
    margen.teleport(-300, 190)
    margen.pendown()
    for i in range(0,2):
        margen.forward(600)
        margen.right(90)
        margen.forward(340)
        margen.right(90)
    margen.penup()
    margen.teleport(-300, -170)
    margen.pendown()
    for i in range(0,2):
        margen.forward(600)
        margen.right(90)
        margen.forward(100)
        margen.right(90)
def fondo():
    screen =turtle.Screen()
    screen.bgcolor("lightblue")
    fondo=turtle.Turtle()
    fondo.speed(0)
    fondo.hideturtle()
    fondo.begin_fill()
    fondo.color("lightgoldenrod3")
    fondo.teleport(-300,-150)
    for _ in range(2):
        fondo.forward(600)
        fondo.left(90)
        fondo.forward(100)
        fondo.left(90)
    fondo.end_fill()
    fondo.penup()
    fondo.teleport(-200,120)
    fondo.color("aquamarine")
    fondo.begin_fill()
    fondo.circle(30)
    fondo.teleport(-225,95)
    fondo.circle(30)
    fondo.teleport(-180,95)
    fondo.circle(30)
    fondo.teleport(180,95)
    fondo.circle(30)
    fondo.teleport(225,95)
    fondo.circle(30)
    fondo.teleport(200,120)
    fondo.circle(30)
    fondo.teleport(0,20)
    fondo.circle(30)
    fondo.teleport(-30,-10)
    fondo.circle(30)
    fondo.teleport(15,-10)
    fondo.circle(30)
    fondo.end_fill()
    fondo.color("darkgreen")
    fondo.begin_fill()
    g=1
    j=-149
    while g<5:
        d=1
        i=-290
        while d<22:
            fondo.teleport(i,j)
            for _ in range(3):
                fondo.forward(10)  
                fondo.left(120) 
            i=i+30
            d=d+1
        j=j+25
        g=g+1
def pez():
    pez=turtle.Turtle()
    pez.speed(300)
    pez.color(a)
    pez.hideturtle()
    pez.penup()
    pez.teleport(x,y)
    pez.pendown()
    pez.begin_fill()
    pez.circle(50)
    pez.end_fill()
    pez.penup()
    pez.teleport(x+100,y)
    pez.pendown()
    pez.setheading(0)
    pez.begin_fill()
    pez.left(150)
    pez.forward(100)
    pez.right(120)
    pez.forward(100)
    pez.right(120)
    pez.forward(100)
    pez.end_fill()
    pez.penup()
    pez.teleport(x-25,y+50)
    pez.pendown()
    pez.color("black")
    pez.begin_fill()
    pez.circle(10)
    pez.end_fill()
def titulo():
    texto=turtle.Turtle()
    texto.hideturtle()
    texto.penup()
    texto.teleport(-140,225)
    texto.pendown()
    texto.write(f"{t}", font=("Arial",16))
def contexto():
    texto=turtle.Turtle()
    texto.hideturtle()
    texto.penup()
    texto.teleport(h,-200-k)
    texto.pendown()
    texto.write(f"{m}", font=("Arial",12))
def cofre():
    cofre=turtle.Turtle()
    cofre.hideturtle()
    cofre.speed(300)
    cofre.penup()
    cofre.teleport(x-400,y-90)
    cofre.pendown()
    cofre.fillcolor("saddlebrown")
    cofre.begin_fill()
    for _ in range(2):
        cofre.forward(200)
        cofre.right(90)
        cofre.forward(100)
        cofre.right(90)
    cofre.end_fill()
    cofre.penup
    cofre.color("black")
    cofre.teleport(x-400,y-120)
    cofre.pendown
    cofre.forward(200)
    cofre.penup
    cofre.color("yellow")
    cofre.teleport(x-308,y-125)
    cofre.pendown
    cofre.begin_fill()
    for _ in range(3):
        cofre.forward(15)
        cofre.left(120)
    cofre.end_fill()

def estrella():
    star=turtle.Turtle()
    star.hideturtle()
    star.speed(300)
    star.teleport(x-300, y-10)
    star.color(a)
    star.begin_fill()
    for _ in range(5):
        star.forward(100)
        star.right(144)
    star.end_fill()
    star.penup
    star.teleport(x-262,y-10)
    star.begin_fill()
    for _ in range(5):
        star.forward(24)
        star.right(72)
    star.end_fill()
def habla():
    bubble = turtle.Turtle()
    bubble.hideturtle()
    bubble.speed(0)
    bubble.penup()
    bubble.teleport(x - 200, y+130)
    bubble.pendown()
    bubble.color("white")
    bubble.begin_fill()
    for _ in range(6):
        bubble.forward(60)
        bubble.right(60)
    bubble.end_fill()
    bubble.penup()
    bubble.teleport(x -210, y +80)
    bubble.pendown()
    bubble.color("black")
    bubble.write(b, font=("Arial", 12))
z=1
print("Hola, bienvenido a nuestro cuenta cuentos")
n=input("Ingresa tu nombre: ")
e=int(input("ingresa tu edad en numeros: "))
print("1) rojo", "2) azul", "3) amarillo", "4) morado", "5) rosado", sep="\n")
c=int(input("ingresa tu color preferido entre los mencionados"))
while z==1:    
    s=int(input("ingrese la escena a la que desea ir: "))
    match s:
        case 1:
            margen()
            fondo()
            t="Un Pez Curioso"
            titulo()
            x=-50
            y=0
            if c==1:
                a="red"
                m=f'había una vez, un pez llamado {n}, tenía {e} años y le encantaba el color rojo'
            elif c==2:
                a="blue"
                m=f'había una vez, un pez llamado {n}, tenía {e} años y le encantaba el color azul'
            elif c==3:
                a="yellow"
                m=f'había una vez, un pez llamado {n}, tenía {e} años y le encantaba el color amarillo'
            elif c==4:
                a="purple"
                m=f'había una vez, un pez llamado {n}, tenía {e} años y le encantaba el color morado'
            elif c==5:
                a="pink"
                m=f'había una vez, un pez llamado {n}, tenía {e} años y le encantaba el color rosado'
            else:
                print("por favor ingrese un color válido")
                z=1
            pez()
            h=-290
            k=0
            contexto()
            z=1
            
        case 2:
            margen()
            fondo()
            t='El Tesoro'
            titulo()
            x=125
            y=50
            if c==1:
               a="red"
            elif c==2:
               a="blue"
            elif c==3:
                a="yellow"
            elif c==4:
                a="purple"
            elif c==5:
                a="pink"
            else:
                print("por favor ingrese un color válido")
                z=1
            pez()
            cofre()
            m= f"{n} salió a jugar al arrecife cuando se encontró un cofre del tesoro"
            h=-290
            k=0
            contexto()
            z=1

        case 3:      
            margen()
            fondo()
            t='La Estrella del Cofre'
            titulo()
            x=150
            y=70
            if c==1:
                a="red"
            elif c==2:
                a="blue"
            elif c==3:
                a="yellow"
            elif c==4:
                a="purple"
            elif c==5:
                a="pink"
            else:
                print("por favor ingrese un color válido")
                z=1
            pez()
            m=f"del cofre salió una estrella que casualmente era del color favorito de {n}"
            cofre()
            estrella()
            h=-290
            k=0
            contexto()
            z=1

        case 4:
            margen()
            fondo()
            t='Una Lección de Vida'
            titulo()
            x=80
            y=20
            if c==1:
                a="red"
            elif c==2:
                a="blue"
            elif c==3:
                a="yellow"
            elif c==4:
                a="purple"
            elif c==5:
                a="pink"
            else:
                print("por favor ingrese un color válido")
                z=1
            pez()
            estrella()
            h=-290
            b='Ten cuidado'
            habla()
            k=0
            m=f"La estrella le dijo a {n} que tuviera cuidado porque, a pesar de que esta vez se"
            contexto()
            k=20
            m='encontró con una estrella amistosa, no siempre tendría la misma suerte y eso podría'
            contexto()
            k=40
            m='hacerle daño.'
            contexto()
        case 5:
            margen()
            fondo()
            t="Un Aprendizaje Valioso"
            titulo()
            x=0
            y=0
            if c==1:
                a="red"
            elif c==2:
                a="blue"
            elif c==3:
                a="yellow"
            elif c==4:
                a="purple"
            elif c==5:
                a="pink"
            else:
                print("por favor ingrese un color válido")
                z=1
            pez()
            h=-290
            k=0
            m=f"Entonces, {n} aprendió que debe ser cuidadoso con los lugares a donde va"
            contexto()
            k=20
            m='porque podría ser peligroso para él y los que lo rodean'
            contexto()
            b='Seré más'
            habla()
            h=-210
            k=-250
            m='cuidadoso'
            contexto()
            z=1
        case _:
            m='Ingresa una escena váida'
            k=400
            contexto()
            z=1
turtle.done
