from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user1_score = 0
        self.user2_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()    
        
        #User 1
        self.goto(100, 200)
        self.write(self.user1_score, align = "center", font = ("Courier", 80, "normal"))
        
        #User 2
        self.goto(-100, 200)
        self.write(self.user2_score, align = "center", font = ("Courier", 80, "normal"))

        
    def user1_point(self):
        self.user1_score += 1  
        self.update_scoreboard()
  
        
    def user2_point(self):
        self.user2_score += 1
        self.update_scoreboard()
    