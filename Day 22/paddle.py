from turtle import Turtle
STARTING_POSITIONS_1 = [(350,0)]
STARTING_POSITIONS_2 = [(-350,0)]

MOVE_DISTANCE = 20
COLOR = "white"
SHAPE = "square"


class Paddle:
    
    def __init__(self, starting_positions):
        self.all_turtles = []
        self.create_paddle(starting_positions)
        self.head = self.all_turtles[0]
        
    def create_paddle(self, positions):
        for position in positions:
            self.add_segment(position)
            
    def add_segment(self,position):
        new_turtle = Turtle(shape= SHAPE)
        new_turtle.shapesize(stretch_len = 1, stretch_wid= 5)
        new_turtle.color(COLOR)
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)      
        
    def up(self):
        new_y = self.head.ycor() + MOVE_DISTANCE
        self.head.goto(self.head.xcor(), new_y)
        
    def down(self):
        new_y = self.head.ycor() - MOVE_DISTANCE
        self.head.goto(self.head.xcor(), new_y)

class User1_paddle(Paddle):
    def __init__(self):
        super().__init__(STARTING_POSITIONS_1)        
        
class User2_paddle(Paddle):
    def __init__(self):
        super().__init__(STARTING_POSITIONS_2)
    