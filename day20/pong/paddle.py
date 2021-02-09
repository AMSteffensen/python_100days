from turtle import Turtle

STARTING_POSITIONS = [(350, 0), (-350, 0)]


class Paddle:
    def __init__(self):
        self.paddles = []
        self.create_paddles()
        self.paddle_one = self.paddles[0]

    def create_paddles(self):
           for position in STARTING_POSITIONS:
            self.add_paddle(position)

    def add_paddle(self, position):
        new_paddle = Turtle(shape="square")
        new_paddle.color("white")
        new_paddle.penup()
        new_paddle.shapesize(3.5, 1)
        new_paddle.goto(position)
        self.paddles.append(new_paddle)

    def up(self):
        print('up')
        self.paddle_one.setheading(90)
        self.paddle_one.forward()
        self.paddle_one[0].goto(20, 20)
    def down(self):
        print('down')


