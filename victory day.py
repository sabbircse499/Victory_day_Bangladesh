import turtle
import time
turtle.hideturtle()


# Set up the screen
screen = turtle.Screen()
screen.title("Flag of Bangladesh")
screen.setup(width=500, height=300)
screen.bgcolor("white")

# Create the turtle
flag = turtle.Turtle()
flag.speed(3)  # Set drawing speed
flag.hideturtle()
# Flag dimensions
height = 300  # Height of the flag
width = 500   # Width of the flag
circle_radius = height * 0.2  # The circle's radius is proportional to the flag's height
circle_center_x = -width * 0.15  # Offset for the circle center (from the rectangle's center)

# Draw the green rectangle (Flag background)
flag.penup()
flag.goto(-width / 2, height / 2)  # Start position (top-left corner)
flag.pendown()
flag.color("green")  # Flag background color
flag.begin_fill()
for _ in range(2):  # Draw rectangle
    flag.forward(width)  # Width of rectangle
    flag.right(90)
    flag.forward(height)  # Height of rectangle
    flag.right(90)
flag.end_fill()

# Draw the red circle (Sun symbol)
flag.penup()
flag.goto(0, -85)  # Center position for the circle
flag.pendown()
flag.color("red")  # Circle color
flag.begin_fill()
flag.circle(100)  # Radius of the circle
flag.end_fill()
flag.hideturtle()



flag.penup()
flag.goto(0, -height / 2 - 40)  # Position the text below the flag
flag.pendown()
flag.color("black")
flag.write('৭১ আমাদের শেকড় ২৪ আমাদের অস্তিত্ব', align="center", font=("Arial", 20, "bold"))

# Hide the turtle and finish
flag.hideturtle()
time.sleep(3)

flag.reset()








rs = turtle.Turtle()
rs.speed(1)  
rs.hideturtle()
rs.penup()
rs.goto(0, -75)  # Center position for the circle
rs.pendown()
rs.color("red")  # Circle color
rs.begin_fill()
rs.circle(100)  # Radius of the circle
rs.end_fill()
rs.hideturtle()



dpen=turtle.Turtle()
dpen.hideturtle()
dpen.width(3)

dpen.color("black")
new=turtle.getscreen()
dpen.speed(5)

new.bgcolor("white")


# Hidden Work(penup)
dpen.left(180)
dpen.penup()
dpen.forward(270)
dpen.left(90)
dpen.forward(200)
dpen.left(180)
dpen.pendown()

dpen.pendown()


# Printing 1

#start to draw
dpen.forward(200)
dpen.right(90)
dpen.forward(55)
dpen.right(90)
dpen.forward(200)
dpen.right(90)
dpen.forward(10)
dpen.right(90)
dpen.forward(190)
dpen.left(90)
dpen.forward(35)
dpen.left(90)
dpen.forward(190)
dpen.right(90)
dpen.forward(10)

dpen.penup()
dpen.left(180)
dpen.forward(75)
dpen.left(90)

dpen.pendown()



# Printing 2

dpen.forward(270)
dpen.right(90)
dpen.forward(55)
dpen.right(90)
dpen.forward(270)
dpen.right(90)
dpen.forward(10)
dpen.right(90)
dpen.forward(260)
dpen.left(90)
dpen.forward(35)
dpen.left(90)
dpen.forward(260)
dpen.right(90)
dpen.forward(10)

dpen.penup()
dpen.left(180)
dpen.forward(110)
dpen.left(90)

dpen.pendown()



# Printing 3
dpen.forward(290)
dpen.left(15)
dpen.forward(150)
dpen.right(105)
dpen.forward(252.6457135)
dpen.right(105)
dpen.forward(150)
dpen.left(15)
dpen.forward(290)
dpen.right(90)
dpen.forward(15)
dpen.right(90)
dpen.forward(290)
dpen.right(15)
dpen.forward(140)
dpen.left(105)
dpen.forward(125.5454112)
dpen.left(100)
dpen.forward(140)
dpen.right(10)
dpen.forward(290)
dpen.right(90)
dpen.forward(15)
dpen.right(90)
dpen.forward(290)
dpen.left(10)
dpen.forward(140)
dpen.left(80)
dpen.forward(76.74131845)
dpen.left(105)
dpen.forward(140)
dpen.right(15)
dpen.forward(290)
dpen.right(90)
dpen.forward(15)

dpen.penup()
dpen.left(180)
dpen.forward(225)
dpen.left(90)

dpen.pendown()




# Printing 4

dpen.forward(270)
dpen.right(90)
dpen.forward(55)
dpen.right(90)
dpen.forward(270)
dpen.right(90)
dpen.forward(10)
dpen.right(90)
dpen.forward(260)
dpen.left(90)
dpen.forward(35)
dpen.left(90)
dpen.forward(260)
dpen.right(90)
dpen.forward(10)

dpen.penup()
dpen.left(180)
dpen.forward(75)
dpen.left(90)

dpen.pendown()



# Printing 1

dpen.forward(200)
dpen.right(90)
dpen.forward(55)
dpen.right(90)
dpen.forward(200)
dpen.right(90)
dpen.forward(10)
dpen.right(90)
dpen.forward(190)
dpen.left(90)
dpen.forward(35)
dpen.left(90)
dpen.forward(190)
dpen.right(90)
dpen.forward(10)



dpen.penup()
dpen.left(90)
dpen.forward(40)
dpen.right(90)
dpen.forward(360)
dpen.left(180)
dpen.forward(50)
dpen.write('Victory day 2024',font=("Arial", 24, "bold"))


# Move down to write the second line
dpen.penup()
dpen.sety(dpen.ycor() - 40)  # Move down by 40 units
dpen.pendown()

# Write "by Sabbir Hossen"
dpen.write(" Develop by Sabbir Hossen", font=("Arial", 12, ))

turtle.done()