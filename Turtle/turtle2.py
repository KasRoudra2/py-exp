import turtle

Turtle = turtle.Turtle()
Screen = turtle.Screen()

Screen.bgcolor("lightgreen")
Screen.title("Turtle Experiment")

Turtle.color("blue", "red")
Turtle.speed(10)

Turtle.penup()
Turtle.goto(-200, 0)
Turtle.pendown()

def star(size):
    if size <= 10:
        print("I return", size)
        return
    else:
        for i in range(5):
            Turtle.forward(size)
            print("I am inside the loop", i, size)
            star(size/4)
            Turtle.right(216)

# Create a star
Turtle.begin_fill()
star(300)
Turtle.end_fill()


turtle.done()