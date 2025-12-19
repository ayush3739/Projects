###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
## colorgram doc:-https://pypi.org/project/colorgram.py/

from turtle import Turtle,Screen
import random
top=Turtle()
sc=Screen()
sc.colormode(255)
top.hideturtle()
colors_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
               (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
                 (54, 45, 50), (101, 75, 77),  (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def random_color():
    rgb=random.choice(colors_list)
    return (rgb)

top.speed("fastest")
top.penup()
top.setheading(225)
top.forward(300)
top.setheading(0)
number_of_dots=100

for i in range(1,number_of_dots+1):
    top.dot(20,random_color())
    top.forward(50)
    if i%10==0:
        top.setheading(90)
        top.forward(50)
        top.setheading(180)
        top.forward(500)
        top.setheading(360)


sc.exitonclick()