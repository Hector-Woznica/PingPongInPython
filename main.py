import turtle 
from setting import positions



def move_left_rod_up():
    if Rod_Left.ycor()<450:
        Rod_Left.forward(20)

def move_left_rod_down():
    if Rod_Left.ycor()>-450:
        Rod_Left.forward(-20)

def move_right_rod_up():
    if Rod_Right.ycor()<450:
        Rod_Right.forward(20)

def move_right_rod_down():
    if Rod_Right.ycor()>-450:
        Rod_Right.forward(-20)

# adjust the screen of gae
Screen = turtle.Screen()
Screen.setup(width=1.0,height=1.0)
Screen.title("Ping Pong Game")


# we dont know functions so we will make adn write code for differetn rods
Rod_Left = turtle.Turtle("square")
Rod_Left.penup()
Rod_Left.shapesize(1,25)
Rod_Left.left(90)
Rod_Left.goto(positions['LEFT_ROD_X_POS'], 0)

Rod_Right = turtle.Turtle("square")
Rod_Right.penup()
Rod_Right.shapesize(1,25)
Rod_Right.left(90)
Rod_Right.goto(positions['RIGHT_ROD_X_POS'], 0)

# try to make ball circle shape , not square
# 
Ball = turtle.Turtle("circle")
Ball.shapesize (3,3)

# turtle can listen keys and on pressing any key you can call a function
turtle.listen()

turtle.onkeypress(move_left_rod_up, "w")
turtle.onkeypress(move_left_rod_down, "s")
turtle.onkeypress(move_right_rod_up, "Up")
turtle.onkeypress(move_right_rod_down, "Down")



    






turtle.mainloop()