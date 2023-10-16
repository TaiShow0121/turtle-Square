import turtle
n = float(input(">"))
turtle.speed(1)
d = 360/n
for i in range(2000):
    turtle.forward(100)
    turtle.left(d)

turtle.done()