import turtle

# set a title for your canvas window
turtle.title('My Turtle Animation')
# set up the screen size (in pixels)
# set the starting point of the turtle (0, 0)
turtle.setup(width=200, height=200, startx=0, starty=0)
# sets the pen color to red
turtle.pencolor('red')

# Draw a square
turtle.speed(10)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)

def setup():
    """ Provide the config for the screen """
    turtle.title('Multiple Squares Animation')
    turtle.setup(100, 100, 0, 0)
    turtle.hideturtle()

def draw_square(size):
    """ Draw a square in the current direction """
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)

setup()
for _ in range(0, 12):
    draw_square(50)
    # Rotate the starting direction
    turtle.right(120)

turtle.title('Filled Square Example')
turtle.setup(100, 100, 0, 0)
turtle.hideturtle()
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.begin_fill()
draw_square(60)
turtle.end_fill()
turtle.done()

# …
# Add this so that the window will close when clicked on
turtle.exitonclick()
