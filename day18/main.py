from turtle import Turtle, Screen
#import screen

t = Turtle()
t.shape("turtle")
t.color("red")

#for i in range(1, 5):
t.begin_fill()
t.penup()
t.goto(-400, 0)
t.pendown()
t.forward(20)
while t.distance(80,00):
    t.penup()
    t.forward(20)
    t.pendown()
    t.forward(20)
t.end_fill()

    


#timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("green")


screen = Screen()
screen.exitonclick()