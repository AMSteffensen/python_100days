from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("brown")
#Pop up, what color
user_bet = screen.textinput(title="Make your bets", prompt="Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_positions = [-80, -40, 0, 40, 80, 120]
all_turtles = []

#line up on start
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=start_positions[turtle_index])
    all_turtles.append(new_turtle)

def write_winning_turtle(winning_color):
    winner = winning_color
    turtle.color('deep pink')
    style = ('Courier', 30, 'italic')
    turtle.write(f"You've won!!{winner}" , 
    font=style, 
    align='center')
    turtle.hideturtle()
    turtle.write() 

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} turtle is the winner!") 
                write_winning_turtle(winning_color) 
            else:
                print(f"You've lost! {winning_color} turtle is the winner!") 
                write_winning_turtle(winning_color) 
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()