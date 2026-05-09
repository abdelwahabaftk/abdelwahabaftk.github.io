# concurs_dibuix_amb_formes_basiques.py
# Concurs de dibuix amb formes bàsiques - Python amb Turtle

import turtle
import random

# Configurar la finestra
screen = turtle.Screen()
screen.title("Concurs de Dibuix amb Formes Bàsiques")
screen.bgcolor("white")

# Crear la tortuga
t = turtle.Turtle()
t.speed(0)  # Velocitat màxima
t.pensize(2)

def dibuixar_cercle(x, y, radi, color):
    """Dibuixa un cercle en una posició específica"""
    t.penup()
    t.goto(x, y - radi)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radi)
    t.end_fill()

def dibuixar_rectangle(x, y, ample, alt, color):
    """Dibuixa un rectangle"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(ample)
        t.left(90)
        t.forward(alt)
        t.left(90)
    t.end_fill()

def dibuixar_triangle(x, y, costat, color):
    """Dibuixa un triangle equilàter"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(costat)
        t.left(120)
    t.end_fill()

def dibuixar_estrella(x, y, mida, color):
    """Dibuixa una estrella"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(mida)
        t.right(144)
    t.end_fill()

# Colors disponibles
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]

# Dibuixar formes aleatòries
print("=== Concurs de Dibuix amb Formes Bàsiques ===")
print("Dibuixant formes aleatòries...")

for i in range(20):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    color = random.choice(colors)

    forma = random.choice(["cercle", "rectangle", "triangle", "estrella"])

    if forma == "cercle":
        radi = random.randint(20, 50)
        dibuixar_cercle(x, y, radi, color)
    elif forma == "rectangle":
        ample = random.randint(30, 80)
        alt = random.randint(20, 60)
        dibuixar_rectangle(x, y, ample, alt, color)
    elif forma == "triangle":
        costat = random.randint(40, 80)
        dibuixar_triangle(x, y, costat, color)
    elif forma == "estrella":
        mida = random.randint(30, 60)
        dibuixar_estrella(x, y, mida, color)

print("Dibuix completat! Tanca la finestra per sortir.")
turtle.done()