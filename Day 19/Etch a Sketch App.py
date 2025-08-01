from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():#
    tim.forward(10)
    
def move_backwards():#
    tim.backward(10)
    
def counter_clockwise():
    tim.circle(1*50)

def clockwise():
    tim.circle(-1*50)

def turn_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)
    
def turn_right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)

def clear_drawing(): #
    tim.reset()  
    
screen.listen()
screen.onkey(key= "w", fun= move_forwards)
screen.onkey(key= "s", fun= move_backwards)
screen.onkey(key= "a", fun= turn_left)
screen.onkey(key= "d", fun= turn_right)
screen.onkey(key= "c", fun= clear_drawing)

screen.exitonclick()
