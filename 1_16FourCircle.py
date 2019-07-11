import turtle


def drawCircle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(100) 

drawCircle(-100, 100)
drawCircle(100, 100)
drawCircle(-100,-100)
drawCircle(100, -100)
