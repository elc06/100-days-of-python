from turtle import Turtle, Screen
import turtle as t
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")
t.colormode(255)

# ## Creating a dash line
# for x in range (0,250,10):
#     tim.forward(5)
#     tim.teleport(x=x)

### Creating different shape & color
# def draw(n):
#     angle = 360/n
#     for side in range(n):
#         tim.forward(100)
#         tim.right(angle)
        
# colors = ["red","orange","gold","lime green","green","deep sky blue","dodger blue","dark violet"]
# for x in range(3,11):
#     tim.color(random.choice(colors))
#     draw(x)


# ## Creating a random walk 
# def random_walk(d):
#     tim.pensize(8)
#     tim.speed("fastest")
#     for r in range (d):
#         tim.color(random_color()) #(random.choice(colors))
#         tim.forward(random.choice(range(1,71)))
#         tim.setheading(random.choice(direction))
# random_walk(100)
        
#Random Color
def random_color():
    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,225)
    color = (r,g,b)
    return color
    
# direction = [0,90,180,270]

tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for x in range (int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+ size_of_gap)
        
draw_spirograph(5)








screen = t.Screen()
screen.exitonclick()