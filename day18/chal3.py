from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()
s.bgcolor("gray")
s.title('hello')

t.shape("turtle")
t.color("black")
t.pensize(1)
t.speed(3500)

#s.textinput("NIM", "Name of first player:")

# change and draw a random color
clrs = ["yellow", "red", "purple", "blue"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for j in range(num_sides):
        angle = 360 / num_sides
        t.forward(100)
        t.left(angle)

for shape_in_side in range(3, 11):
    for c in clrs: 
        t.color(c) 
        draw_shape(shape_in_side)
        
        
           


# draw pentagon, hexagon, heptgon, octagon, nonagon, decagon

    


#timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("green")


screen = Screen()
screen.exitonclick()