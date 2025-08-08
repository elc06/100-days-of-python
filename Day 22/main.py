from turtle import Screen
from paddle import User1_paddle, User2_paddle
from ball import Ball
from score_board import Score_board
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

user1_paddle = User1_paddle()
user2_paddle = User2_paddle()
ball = Ball()
scoreboard = Score_board()

screen.listen()
screen.onkey(user1_paddle.up,"Up")
screen.onkey(user1_paddle.down,"Down")
screen.onkey(user2_paddle.up,"w")
screen.onkey(user2_paddle.down,"s")

game_mode = True

while game_mode:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
    #Wall top-bottom boundary
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
        
    #Ball contact with user1_paddle
    if (ball.distance(user1_paddle.head) < 50 and ball.xcor() > 320) or (ball.distance(user2_paddle.head) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    
    #User 1 missed
    if ball.xcor() > 380: 
            ball.reset_position() 
            scoreboard.user2_point()
            
    #User 2 missed
    if ball.xcor() < -380:
            ball.reset_position()   
            scoreboard.user1_point()
            
screen.exitonclick() 