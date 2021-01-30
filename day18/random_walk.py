from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()
s.bgcolor("gray")
s.title('hello')
s.colormode(255)

t.shape("turtle")
t.color("yellow")
t.pensize(10)
t.speed("fastest")

# change and draw a random color
clrs = ["yellow", "red", "purple", "blue"]
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    colors = (r, g, b)
    return colors

for _ in range(200):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))

def get_random():
    return random.randint(0,3)

def move_random(direction): 
   #for i in range(0, 10):
    if direction == 1:
        t.forward(20)
    elif direction == 2:
        t.left(20)
    elif direction == 3: 
        t.right(20)
        
for _ in range(0, 999999):
    direction = get_random()
    t.color(random.choice(clrs)) 
    move_random(direction)

screen = Screen()
screen.exitonclick()


