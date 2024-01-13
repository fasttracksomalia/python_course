import turtle

def draw_somalia():
    screen = turtle.Screen()
    screen.bgcolor("white")

    turtle.speed(2)
    turtle.pensize(2)
    turtle.color("black")

    # Draw the outline of Somalia
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(200)
    turtle.end_fill()

    # Draw the flag of Somalia
    draw_somalia_flag()

    turtle.hideturtle()
    screen.mainloop()

def draw_somalia_flag():
    turtle.penup()
    turtle.goto(-120, 70)
    turtle.pendown()

    # Draw the blue background of the flag
    turtle.color("#0072C6")  # Hex code for the blue color
    turtle.begin_fill()
    turtle.forward(240)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(240)
    turtle.right(90)
    turtle.forward(40)
    turtle.end_fill()

    # Draw the white star in the flag
    draw_white_star()

def draw_white_star():
    turtle.penup()
    turtle.goto(-100, 80)
    turtle.pendown()
    turtle.color("white")

    # Draw the five-pointed star
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(40)
        turtle.right(144)
        turtle.forward(40)
        turtle.left(72)
    turtle.end_fill()

if __name__ == "__main__":
    draw_somalia()
