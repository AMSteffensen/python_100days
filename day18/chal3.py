from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()
s.bgcolor("gray")
s.title('hello')


t.shape("turtle")
t.color("black")
t.pensize(10)
t.speed(3500)
s.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    colors = (r, g, b)
    return colors

print(random_color())
# draw pentagon, hexagon, heptgon, octagon, nonagon, decagon
def draw_shape(num_sides):
    angle = 360 / num_sides
    for j in range(num_sides):
        angle = 360 / num_sides
        t.forward(100)
        t.left(angle)

for shape_in_side in range(3, 11):
    t.pencolor(random_color())
    draw_shape(shape_in_side)

screen = Screen()
screen.exitonclick()