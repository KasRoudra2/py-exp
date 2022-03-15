import turtle

Turtle = turtle.Turtle()
Screen = turtle.Screen()

Screen.bgcolor("lightgreen")
Screen.title("Turtle Experiment")

Turtle.color("blue", "red")
Turtle.speed(10)



# Create a star
Turtle.begin_fill()
for i in range(47):
    Turtle.forward(150)
    Turtle.right(168.5)
Turtle.end_fill()

# Creating a new disconnected shape
Turtle.penup()
Turtle.goto(-250,-50)
Turtle.pendown()

# Create a star
Turtle.begin_fill()
for i in range(5):
    Turtle.forward(200)
    Turtle.right(216)
Turtle.end_fill()


turtle.done()