# 🎨 Hirst Painting using Turtle Graphics
# This program creates a beautiful dot painting inspired by artist Damien Hirst.
# Each dot is randomly colored from a palette extracted from an image.
import turtle
from turtle import Turtle, Screen
import random
import colorgram

# Optional: colorgram can extract colors from an image
# (uncomment and use if you have colorgram installed and an image file)

rgb_colors = []
colors = colorgram.extract('hirst.jpg', 50)
for color in colors:
     r = color.rgb.r
     g = color.rgb.g
     b = color.rgb.b
     rgb_colors.append((r, g, b))


# Set color mode to RGB (0–255)
turtle.colormode(255)

# Predefined color palette (manually extracted from an image)
# rgb_colors = [
#     (238, 224, 203), (204, 157, 106), (172, 71, 36), (233, 216, 224),
#     (217, 218, 226), (227, 208, 117), (141, 145, 160), (95, 104, 135),
#     (192, 151, 170), (183, 152, 41), (223, 229, 224), (32, 34, 14),
#     (19, 26, 61), (97, 115, 173), (221, 172, 195), (173, 28, 9),
#     (22, 36, 20), (121, 105, 113), (197, 98, 74), (234, 174, 160),
#     (144, 151, 146), (101, 109, 103), (41, 51, 100), (182, 184, 214),
#     (172, 104, 122), (46, 29, 45), (73, 72, 41), (232, 203, 16),
#     (121, 38, 50), (55, 71, 54), (122, 131, 125), (184, 197, 187),
#     (123, 129, 131), (189, 193, 194)
# ]

# Create turtle object
tim = Turtle()
tim.speed(0)          # Fastest drawing speed
tim.penup()           # Prevent drawing lines
tim.hideturtle()      # Hide turtle cursor for a clean output

# Move turtle to bottom-left corner of the canvas
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Draw 10x10 grid of colored dots
total_no_of_dots = 101
for dot_count in range(1, total_no_of_dots):
    tim.dot(15, random.choice(rgb_colors)) # Draw a colored dot
    tim.forward(50)  # Space between dots

    # Move up to next row every 10 dots
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# Keep window open until clicked
screen = Screen()
screen.exitonclick()
