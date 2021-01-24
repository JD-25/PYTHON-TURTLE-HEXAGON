import turtle
x = turtle.Screen()

hexagon = turtle.Turtle()

# To change the coordinates of the HEXAGON:
# hexagon.penup()
# hexagon.goto(-100, 50)
# hexagon.pendown()

for i in range(6):
    hexagon.pensize(5.5)
    hexagon.pencolor("red")
    hexagon.forward(90)
    hexagon.left(300)

hexagon.penup()
hexagon.goto(100, -50)
hexagon.pendown()
hexagon.speed(6)

for i in range(6):
    hexagon.pensize(5.5)
    hexagon.pencolor("blue")
    hexagon.forward(90)
    hexagon.left(300)