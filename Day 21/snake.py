from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def extend_body(self):
        self.add_segment(self.all_turtles[-1].position())
        
    def add_segment(self,position):
        new_turtle = Turtle(shape= "square")
        new_turtle.shapesize(stretch_len = 1, stretch_wid= 1)
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)            
            
            
    def move(self):
        for tur in range(len(self.all_turtles) -1, 0, -1):
            new_x_position = self.all_turtles[tur - 1].xcor()
            new_y_position = self.all_turtles[tur - 1].ycor()
            self.all_turtles[tur].goto(new_x_position,new_y_position)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
       if self.head.heading() != DOWN:
           self.head.setheading(UP)
        
    def down(self):
       if self.head.heading() != UP:
           self.head.setheading(DOWN)
           
    def left(self):
       if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)
           
    def right(self):
        if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)
           
