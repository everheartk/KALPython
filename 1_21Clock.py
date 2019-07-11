import turtle

#draw the clock and arms
turtle.goto(0,0)
turtle.circle(100)
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.goto(0,175)
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.goto(75,100)

#Note the 12, 3, 6, 9
turtle.penup()
turtle.goto(-2,185)
turtle.write("12")

turtle.penup()
turtle.goto(85,98)
turtle.write("3")

turtle.penup()
turtle.goto(-2,2)
turtle.write("6")

turtle.penup()
turtle.goto(-85,98)
turtle.write("9")

#print time at the bottom
turtle.penup()
turtle.goto(-15,-15)
turtle.write("9:15:00")
