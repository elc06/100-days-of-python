# import colorgram 

# # Extract 6 colors from an image.
# colors = colorgram.extract("Day 18/hirst_image.jpg", 31)

# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34

# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))

# print(rgb_colors)

from turtle import Turtle, Screen
import turtle as t
import random

tim = Turtle()

tim.color("white")
t.colormode(255)  

color_list= [ (203, 172, 108), (220, 227, 234), (237, 245, 242), (153, 180, 195), (152, 186, 174), (193, 161, 176), (214, 203, 113), (208, 179, 195), (174, 188, 213), (161, 213, 187), (161, 203, 215), (114, 123, 186), (177, 160, 71), (213, 182, 181), (198, 207, 46), (105, 114, 142), (164, 121, 51)]
tim.speed("fastest")
tim.setposition(-250, -250)

## Creating dot 
for row in range(11):
    for col in range (11):
        x = -250 + col * 50
        y = -250 + row * 50
        tim.teleport(x,y)
        tim.dot(20, random.choice(color_list))
    
        
screen = t.Screen()
screen.exitonclick()