import turtle

# Configuração inicial
screen = turtle.Screen()
screen.bgcolor("lightgray")
tank = turtle.Turtle()
tank.speed(5)
tank.width(3)

# Função para desenhar um retângulo
def draw_rectangle(width, height):
    for _ in range(2):
        tank.forward(width)
        tank.left(90)
        tank.forward(height)
        tank.left(90)

# Função para desenhar um círculo
def draw_circle(radius):
    tank.circle(radius)

# Função para desenhar as esteiras do tanque
def draw_tracks():
    tank.penup()
    tank.goto(-100, -50)
    tank.pendown()
    draw_rectangle(200, 30)  # Esteira esquerda
    tank.penup()
    tank.goto(-100, 20)
    tank.pendown()
    draw_rectangle(200, 30)  # Esteira direita

# Função para desenhar a carroceria do tanque
def draw_body():
    tank.penup()
    tank.goto(-80, -20)
    tank.pendown()
    tank.fillcolor("green")
    tank.begin_fill()
    draw_rectangle(160, 60)
    tank.end_fill()

# Função para desenhar a torre do tanque
def draw_turret():
    tank.penup()
    tank.goto(-20, 40)
    tank.pendown()
    tank.fillcolor("darkgreen")
    tank.begin_fill()
    draw_rectangle(40, 40)
    tank.end_fill()

# Função para desenhar o canhão do tanque
def draw_gun():
    tank.penup()
    tank.goto(0, 60)
    tank.pendown()
    tank.setheading(0)
    tank.forward(60)
    tank.backward(60)

# Função para desenhar as rodas do tanque
def draw_wheels():
    wheel_positions = [(-80, -50), (-40, -50), (0, -50), (40, -50), (80, -50),
                       (-80, 20), (-40, 20), (0, 20), (40, 20), (80, 20)]
    for pos in wheel_positions:
        tank.penup()
        tank.goto(pos)
        tank.pendown()
        tank.fillcolor("black")
        tank.begin_fill()
        draw_circle(10)
        tank.end_fill()

# Desenhar o tanque
draw_tracks()
draw_body()
draw_turret()
draw_gun()
draw_wheels()

# Finalizar
tank.hideturtle()
screen.mainloop()