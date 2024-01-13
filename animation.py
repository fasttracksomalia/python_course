import turtle
import random

# Function to draw a colorful star
def draw_colorful_star(size):
    turtle.color("red", "yellow")  # Set the fill and border colors
    turtle.begin_fill()  # Start filling the shape

    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

    turtle.end_fill()  # End filling the shape

# Set up the Turtle window
turtle.speed(2)  # Set the drawing speed
turtle.bgcolor("black")  # Set the background color

# Draw multiple colorful stars
for _ in range(5):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    size = random.randint(50, 150)
    draw_colorful_star(size)

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()
