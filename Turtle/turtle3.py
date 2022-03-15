import turtle

Turtle = turtle.Turtle()
Screen = turtle.Screen()

Screen.bgcolor("lightgreen")
Screen.title("Turtle Experiment")

Turtle.color("blue", "red")
Turtle.speed(100)

Turtle.penup()
Turtle.goto(-100, -135)
Turtle.pendown()
Turtle.left(35)

def star(size):
    if size <= 10:
        return
    else:
        for i in range(5):
            Turtle.forward(size)
            star(size/3)
            Turtle.right(216)

# Create a star
Turtle.begin_fill()
try:
    star(300)
except:
    exit()
Turtle.end_fill()


turtle.done()