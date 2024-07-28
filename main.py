import tkinter
import turtle as turtle_module
import random
import colorgram
# library that lets you extract colors from images.
# Compared to other libraries, the colorgram algorithm’s results are more intense

turtle_module.colormode(255)
tim = turtle_module.Turtle()

# colors = colorgram.extract("20_001.jpg", 15)
# first_color = colors[0]
# rgb = first_color.rgb

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48)]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")


for dot_count in range(1, 101):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()