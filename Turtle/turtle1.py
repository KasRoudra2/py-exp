import turtle

Turtle = turtle.Turtle()
Screen = turtle.Screen()

Screen.bgcolor("lightgreen")
Screen.title("Turtle Experiment")

Turtle.color("blue", "red")
Turtle.speed(2)

# Draw a square
Turtle.begin_fill()
Turtle.forward(100)
Turtle.left(90)
Turtle.forward(100)
Turtle.left(90)
Turtle.forward(100)
Turtle.left(90)
Turtle.forward(100)
Turtle.end_fill()


# Doing a reverse square
Turtle.backward(100)
Turtle.right(90)
Turtle.backward(100)
Turtle.right(90)
Turtle.backward(100)
Turtle.right(90)
Turtle.backward(100)


turtle.done()