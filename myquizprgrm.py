import turtle

# Initialize the turtle
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(5)

# Draw the bird's body
pen.penup()
pen.goto(-50, -50)
pen.pendown()
pen.circle(50)

# Draw the head
pen.penup()
pen.goto(20, 20)
pen.pendown()
pen.circle(30)

# Draw the beak
pen.penup()
pen.goto(50, 30)
pen.pendown()
pen.goto(70, 40)
pen.goto(50, 45)
pen.goto(50, 30)

# Draw wings
pen.penup()
pen.goto(-50, 0)
pen.pendown()
pen.goto(-100, 50)
pen.goto(-50, 50)
pen.goto(-50, 0)

# Draw tail
pen.penup()
pen.goto(-50, -50)
pen.pendown()
pen.goto(-80, -80)
pen.goto(-50, -70)

# Hide turtle and display window
pen.hideturtle()
turtle.done()
