from turtle import Turtle, Screen
import random
game_mode = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Turtle Racing Game", prompt= "Which turtle will be the winner? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "SkyBlue", "blue", "purple"]
y_positions = [-90,-60, -30, 0, 30, 60, 90]

all_turtles = []

for index in range(7):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-200, y=y_positions[index])
    all_turtles.append(new_turtle)

if user_bet:
    game_mode = True
    
while game_mode:
    for turtle in all_turtles:
        if turtle.xcor() >= 200:
            game_mode = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You won!! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You lose... :( The {winning_turtle} turtle is the winner.)")
        
        random_distance = random.randint(1,10)
        turtle.forward(random_distance)

screen.exitonclick()