from turtle import Screen
from turtle import Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

paddle = Paddle()

screen.listen()
screen.onkey(paddle.up, "w")
screen.onkey(paddle.down, "s")













screen.exitonclick()