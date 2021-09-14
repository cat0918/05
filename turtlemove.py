import turtle
def forw():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
def right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
def under():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
def left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(forw, 'w')
turtle.onkey(right, 'd')
turtle.onkey(under, 's')
turtle.onkey(left, 'a')
turtle.onkey(restart, 'Escape')
turtle.listen()
