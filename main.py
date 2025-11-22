import turtle
from turtle import Turtle, Screen




def move_left_rod_up():
    if Rod_Left.ycor()<450:
        rod_positions[0] = True
        

def move_left_rod_down():
    if Rod_Left.ycor()>-450:
        rod_positions[1] = True

def move_right_rod_up():
    if Rod_Right.ycor()<450:
        rod_positions[2] = True
def move_right_rod_down():
    if Rod_Right.ycor()>-450:
        rod_positions[3] = True

screen = Screen()
screen.setup(width=1.0,height=1.0)
# get screen size
screen_width = screen.window_width()
screen_height = screen.window_height()

rodleft_position = (-screen_width/2 + 50, 0)
rodright_position = (screen_width/2 - 50, 0)



print(screen_width, screen_height)
screen.title("Ping Pong Game")


# we dont know functions so we will make adn write code for differetn rods
Rod_Left = Turtle("square")
Rod_Left.penup()
Rod_Left.shapesize(1,25)
Rod_Left.left(90)
Rod_Left.goto(rodleft_position)

Rod_Right = Turtle("square")
Rod_Right.penup()
Rod_Right.shapesize(1,25)
Rod_Right.left(90)
Rod_Right.goto(rodright_position)

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

turtle.onkeyrelease(lambda: rod_positions.__setitem__(0, False), "w")  # hector
turtle.onkeyrelease(lambda: rod_positions.__setitem__(1, False), "s")  # hector
turtle.onkeyrelease(lambda: rod_positions.__setitem__(2, False), "Up")  # hector
turtle.onkeyrelease(lambda: rod_positions.__setitem__(3, False), "Down")  # hector

rod_positions = [False, False, False, False]  # [left_up, left_down, right_up, right_down]
# keep checking positioons 


# keep checking about 100 millisec rod positions
def check_rod_positions():
    if rod_positions[0]:
        Rod_Left.sety(Rod_Left.ycor() + 20)
    if rod_positions[1]:
        Rod_Left.sety(Rod_Left.ycor() - 20)
    if rod_positions[2]:
        Rod_Right.sety(Rod_Right.ycor() + 20)
    if rod_positions[3]:
        Rod_Right.sety(Rod_Right.ycor() - 20)
    turtle.ontimer(check_rod_positions, 100)
check_rod_positions()




turtle.mainloop()