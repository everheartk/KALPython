import turtle

#create first rectangle
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)

#create 2nd rectangle
turtle.penup()
turtle.right(90)
turtle.goto(20, 20)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)

#connect the rectangles
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(20,20)

turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.goto(120,20)

turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.goto(20,-30)

turtle.penup()
turtle.goto(100,-50)
turtle.pendown()
turtle.goto(120,-30)



